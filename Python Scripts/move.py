#MicroPython on a rp2040 script to move the motors to the correct position of the grid
#The function takes the current position, the size of the grid, and where we want to move to
#It then figures out how many step it will take to move there and moves the motors accordingly

import machine
import _thread
from machine import Pin
from time import sleep_ms
import functions
import calibration

#Interrupt handlers for buttons to start calibration and movement
#pins 14 and 15 are used for the buttons, but can be changed if needed
pinCalibrate = Pin(14, Pin.IN, Pin.PULL_DOWN)
pinMove = Pin(15, Pin.IN, Pin.PULL_DOWN)

def enableCalibration(pin):
        global enableCalibrate
        enableCalibrate = True
        print('Calibration started')

pinCalibrate.irq(trigger=Pin.IRQ_RISING, handler=enableCalibration)

def enableMovement(pin):
    global enableMove
    enableMove = True
    print('Movement started')

pinMove.irq(trigger=Pin.IRQ_RISING, handler=enableMovement)

enableCalibrate = False
enableMove = False

#find how to get to new position baised on current position
def move(coordIndex, motor, size, bin, numOfBins):
    positionOld = functions.coord[coordIndex]
    numOfPoints = numOfBins * 2
    sizeOfPoints = size / numOfPoints
    positionNew = sizeOfPoints * ((bin * 2) - 1)
    distanceToMove = int(positionNew - positionOld)
    if distanceToMove > 0:
        for i in range(distanceToMove):
            functions.fullstep_forward(motor)
            functions.mSleep(motor)
    elif distanceToMove < 0:
        for i in range(-distanceToMove):
            functions.fullstep_backward(motor)
            functions.mSleep(motor)
    functions.coord[coordIndex] = positionOld + distanceToMove


#main function to run movement sequence for both x and y axies
def main():
    #initialize manualy for now
    functions.coord[functions.x] = 100
    sizeX = 300
    #sizeY = 300
    numOfBinsX = 12
    #numOfBinsY = 8

    #Where we want to move to
    binX = 4
    #binY = 6

    global enableCalibrate, enableMove

    while(1):

        if enableCalibrate:
            calibration.main()
            enableCalibrate = False

        if enableMove and (enableCalibrate == False):
            def thread1():
                move(functions.x, functions.motor1, sizeX, binX, numOfBinsX)
            _thread.start_new_thread(thread1, ())

            #move(functions.y, functions.motor2, sizeY, binY, numOfBinsY)
            enableMove = False

if __name__ == "__main__":
    main()
