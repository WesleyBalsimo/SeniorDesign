from machine import Pin
from time import sleep_ms
import functions

def main():
    while 1:
        functions.fullstep_forward()

if __name__ == "__main__":
    main()