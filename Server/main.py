from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketState

from pathlib import Path

import csv
from io import StringIO
from queue import Queue
import asyncio
from threading import Lock

# TODO: Remove
from time import sleep, time
from random import randint

MOVEMENT_DELAY_S = 30.0

queue_data = []
queue_lock = Lock()
password_actual = Path("password.txt").read_text().strip() 

def issue_request(location: str, ws: WebSocket) -> int:
    with queue_lock:
        position = len(queue_data) 
        queue_data.append((location, ws))
        return position

async def poll_queue():
    print(5)
    while True:
        location, ws = None
        with queue_lock:
            if len(queue_data) > 0:
                location, ws = queue_data.pop(0)

        print(location)
        if location == None:
            sleep(0.1)
            continue
        
        # ---- TODO: Replace with motor control code ----
        print(location)
        # -----------------------------------------------

        if ws.client_state != WebSocketState.DISCONNECTED:
            ws.send_bytes(b"\x01")

        with queue_lock:
            for i, (l, w) in enumerate(queue_data):
                w.send_bytes(b"\x00" + i.to_bytes(1))

        sleep(MOVEMENT_DELAY_S)

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = None
        try:
            data = await ws.receive_bytes()
        except:
            if ws.client_state != WebSocketState.DISCONNECTED:
                await ws.close()
            break
        if data[0] == 0x00:
            location = data[1:3].decode("utf-8")
            position = issue_request(location, ws)
            
            if position > 0:
                ws.send_bytes(b"\x00" + position.to_bytes(1))
        elif data[0] == 0x01:
            i = 1
            
            password_len = data[i]
            i += 1

            password = data[i:i+password_len].decode("utf-8")
            i += password_len

            csv_new = data[i:].decode("utf-8")

            if password != password_actual:
                await ws.send_bytes(b"\x02")
                continue

            csv_io = StringIO(csv_new)
            reader = csv.reader(csv_io)

            invalid_line = -1
            for line, row in enumerate(reader, 1):
                if len(row) != 3:
                    print("Error: Unexpected row length of", len(row))
                    invalid_line = line
                    break

            if invalid_line != -1:
                await ws.send_bytes(b"\x04" + invalid_line.to_bytes(2, "big"))
                continue

            Path("pub/data.csv").write_text(csv_new)
            
            await ws.send_bytes(b"\x03");
        else:
            await ws.send_bytes(b"\x04")

@app.get("/")
async def root():
    return FileResponse("pub/index.html")

app.mount("/static", StaticFiles(directory="pub", html=True), name="static")
app.mount("/images", StaticFiles(directory="pub/images"), name="static")

@asynccontextmanager
async def startup():
    print(1)
    app.state.task = asyncio.create_task(poll_queue())
    print(2)
    yield
    print(3)
    app.state.task.cancel()
    print(4)
