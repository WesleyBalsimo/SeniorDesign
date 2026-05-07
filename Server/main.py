from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_bytes()
        if data[0] != 0x00:
            ws.send_bytes([0x04])
        location = data[1:2]
        print(location.decode("utf-8"))

@app.get("/")
async def root():
    return FileResponse("pub/index.html")

app.mount("/static", StaticFiles(directory="pub", html=True), name="static")
app.mount("/images", StaticFiles(directory="pub/images"), name="static")
