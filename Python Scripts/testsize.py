import machine
from machine import Pin
from time import sleep_ms
import functions

def sizeTest(pin, motor):
    size = 0
    while pin.value() == 0:
        functions.halfstep_backward(motor)
        size = size + 1
    functions.coord[0] = 0
    functions.sleep(motor)


def main():
    sizeTest(functions.pin_x, functions.motor1)

if __name__ == "__main__":
    main()