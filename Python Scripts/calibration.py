import machine
from machine import Pin
from time import sleep_ms
import functions

#enumeration for on and off
on = 1
off = 0

def calibrate(pin, motor, coord):
    size = 0

    while pin.value() == 0:
        functions.fullstep_forward(motor)
        size = size + 1
    functions.coord[coord] = size
    functions.sleep(motor)
    print('size of ' + str(coord) + ': ' + str(size))

#Main function to run calibration sequence for both x and y axes
def main():
    lights = on
    functions.boardlight(lights)

    calibrate(functions.pin_x, functions.motor1, functions.x)
    
    lights = off
    functions.boardlight(lights)
    print(functions.coord[functions.x])
    print(functions.coord[functions.y])

if __name__ == "__main__":
    main()