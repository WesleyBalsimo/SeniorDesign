import machine
from machine import Pin
from time import sleep_ms
import functions

def calibrate(pin, motor):
    while pin.value() == 0:
        functions.halfstep_backward(motor)
    functions.coord[0] = 0
    functions.sleep(motor)

def main():
    calibrate(functions.pin_x, functions.motor1)

if __name__ == "__main__":
    main()