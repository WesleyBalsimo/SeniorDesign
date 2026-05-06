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

#Main function to run calibration sequence for both x and y axes
def main():

    calibrate(functions.pinLimit_x, functions.motor1, functions.x)
    #calibrate(functions.pinLimit_y, functions.motor2, functions.y)

    print('X Coordinate: ' + str(functions.coord[functions.x]))
    print('Y Coordinate: ' + str(functions.coord[functions.y]))

if __name__ == "__main__":
    main()