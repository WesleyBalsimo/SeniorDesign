import machine
import _thread
from machine import Pin
from time import sleep_ms
import functions


#find the distance from the origin to the point to move to
def distance(size, bin, binNum):
    numOfPoints = binNum * 2
    sizeOfPoints = size / numOfPoints
    distanceToMove = sizeOfPoints * ((bin * 2) - 1)
    return distanceToMove

#find how to get to new position baised on current position
def move(coord, motor, size, bin, binNum):
    positionOld = functions.coord[coord]
    positionNew = distance(size, bin, binNum)
    distanceToMove = positionNew - positionOld
    if distanceToMove > 0:
        for i in range(distanceToMove):
            functions.fullstep_backward(motor)
<<<<<<< HEAD
            functions.mSleep(motor)
    elif distanceToMove < 0:
        for i in range(-distanceToMove):
            functions.fullstep_forward(motor)
            functions.mSleep(motor)
=======
    elif distanceToMove < 0:
        for i in range(-distanceToMove):
            functions.fullstep_forward(motor)
>>>>>>> 8d59dcb2e888be2b564416336eb0ae013b69ac0e
    functions.coord[coord] = positionNew


#main function to run movement sequence for both x and y axes
def main():
    #initialize manualy for now
<<<<<<< HEAD
    functions.coord = 100
    sizeX = 300
    sizeY = 300
=======
    functions.coord = 650
    sizeX = 600
    sizeY = 600
>>>>>>> 8d59dcb2e888be2b564416336eb0ae013b69ac0e
    numOfBinsX = 12
    numOfBinsY = 8

    #Where we want to move to
    binX = 4
    binY = 6

    def thread1():
        move(functions.coord[functions.x], functions.motor1, sizeX, numOfBinsX, binX)
    _thread.start_new_thread(thread1, ())

    move(functions.coord[functions.y], functions.motor2, sizeY, numOfBinsY, binY)

if __name__ == "__main__":
    main()
