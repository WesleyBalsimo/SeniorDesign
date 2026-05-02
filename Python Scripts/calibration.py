from machine import Pin
from time import sleep_ms
import functions

pin9 = machine.Pin(9, Pin.IN)

def main():
    while pin9.value() == 0:
        functions.halfstep_backward(functions.motor1)
    
    

if __name__ == "__main__":
    main()