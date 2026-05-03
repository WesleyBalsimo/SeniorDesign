import machine
from machine import Pin
from time import sleep_ms
import functions

def calibrate(pin, motor, coord):
    while pin.value() == 0:
        functions.halfstep_backward(motor)
    functions.coord[coord] = 0
    functions.sleep(motor)

def main():
    calibrate(functions.pin_x, functions.motor1, functions.x)

if __name__ == "__main__":
    main()