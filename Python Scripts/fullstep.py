# This is mostly a test file to debug and showcase movement

from machine import Pin
from time import sleep
import functions
  
def main():
    size = 0
    while(size < 100):
        functions.fullstep_forward(functions.motor1)
        size = size + 1
    functions.mSleep(functions.motor1)
    size = 0
    sleep(1)

    while(size < 100):
        functions.halfstep_forward(functions.motor1)
        size = size + 1
    functions.mSleep(functions.motor1)
    size = 0
    sleep(1)

    while(size < 100):
        functions.fullstep_forward(functions.motor1)
        size = size + 1
    functions.mSleep(functions.motor1)
    size = 0
    sleep(1)

    while(size < 100):
        functions.halfstep_backward(functions.motor1)
        size = size + 1
    functions.mSleep(functions.motor1)
    size = 0
    sleep(1)

    print(size)

if __name__ == "__main__":
    main()