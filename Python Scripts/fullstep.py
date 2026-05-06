# This is mostly a test file to debug and showcase movement


from machine import Pin
from time import sleep_ms
import functions
  
def main():
    size = 0
    while(1):
        functions.fullstep_forward(functions.motor1)
        size = size + 1
    functions.sleep(functions.motor1)
    print(size)

if __name__ == "__main__":
    main()