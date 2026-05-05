#Outdated version of calibration script

import machine
from machine import Pin
from time import sleep_ms
import functions

pin14 = machine.Pin(14, Pin.OUT)
pin14 = 1

def sizeTest(pin, motor, coord):
    size = 0
    while pin.value() == 0:
        functions.halfstep_backward(motor)
        size = size + 1
    functions.coord[coord] = 0
    functions.sleep(motor)
    print('size of ' + str(coord) + ': ' + str(size))


def main():
    sizeTest(functions.pin_x, functions.motor1, functions.x)

if __name__ == "__main__":
    main()