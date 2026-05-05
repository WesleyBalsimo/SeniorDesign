import machine
from machine import Pin
from time import sleep_ms
import functions

pin14 = machine.pin(14, Pin.OUT)
pin14 = 1

def calibrate(pin, motor, coord):
    size = 0
    while pin.value() == 0:
        functions.quarterstep_forward(motor)
        size = size + 1
    functions.coord[coord] = 0
    functions.sleep(motor)
    print('size of ' + str(coord) + ': ' + str(size))

def main():
    calibrate(functions.pin_x, functions.motor1, functions.x)

if __name__ == "__main__":
    main()