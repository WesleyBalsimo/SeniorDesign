from machine import Pin
from time import sleep_ms
import functions

def main():
    while 1:
        functions.fullstep_forward(functions.motor1)
        functions.sleep(functions.motor1)

if __name__ == "__main__":
    main()