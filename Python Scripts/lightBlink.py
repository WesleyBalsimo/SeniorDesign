#This is a test script to make sure the board is working

from machine import Pin, bitstream
from time import sleep

def boardlight():
	timing = [300, 900, 700, 500]
	np = Pin(16, Pin.OUT)
	red = bytearray([0,20,0])
	green = bytearray([20,0,0])
	blue = bytearray([0,0,20])
	while(1):
    		bitstream(np, 0, timing, red)
    		sleep(1)
    		bitstream(np, 0, timing, green)
    		sleep(1)
    		bitstream(np, 0, timing, blue)
    		sleep(1)