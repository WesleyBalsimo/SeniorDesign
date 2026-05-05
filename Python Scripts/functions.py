import machine
from machine import Pin, bitstream
from time import sleep_ms, sleep

#global x, y coordinates
coord = [0, 0]
#enumeration for x and y coordinates
x = 0 # coord[x] --> coord[0]
y = 1 # coord[y] --> coord[1]

# Motor output

#motor 1 output pins
pin0 = machine.Pin(0, Pin.OUT)
pin1 = machine.Pin(1, Pin.OUT)
pin2 = machine.Pin(2, Pin.OUT)
pin3 = machine.Pin(3, Pin.OUT)

motor1 = [pin0, pin1, pin2, pin3]

#motor 2 output pins
pin4 = machine.Pin(4, Pin.OUT)
pin5 = machine.Pin(5, Pin.OUT)
pin6 = machine.Pin(6, Pin.OUT)
pin7 = machine.Pin(7, Pin.OUT)

motor2 = [pin4, pin5, pin6, pin7]

pin_x = machine.Pin(8, Pin.IN, machine.Pin.PULL_UP)
pin_y = machine.Pin(9, Pin.IN, machine.Pin.PULL_UP)


#define motor positions for full step and half step sequences
def pos1(motor):
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(1)

def pos1_5(motor):
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(1)
    motor[3].value(1)   

def pos2(motor):
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(1)
    motor[3].value(0)

def pos2_5(motor):
    motor[0].value(0)
    motor[1].value(1)
    motor[2].value(1)
    motor[3].value(0)

def pos3(motor):
    motor[0].value(0)
    motor[1].value(1)
    motor[2].value(0)
    motor[3].value(0)

def pos3_5(motor):
    motor[0].value(1)
    motor[1].value(1)
    motor[2].value(0)
    motor[3].value(0)

def pos4(motor):
    motor[0].value(1)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(0)

def pos4_5(motor):
    motor[0].value(1)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(1)

def sleep(motor):
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(0)

#define movement functions for full step and half step sequences
def quarterstep_forward(motor):
    pos1(motor)
    sleep_ms(3)
    pos2(motor)
    sleep_ms(3)
    pos3(motor)
    sleep_ms(3)
    pos4(motor)
    sleep_ms(3)

def fullstep_forward(motor):
    pos1(motor)
    sleep_ms(3)
    pos1_5(motor)
    sleep_ms(3)
    pos2(motor)
    sleep_ms(3)
    pos2_5(motor)
    sleep_ms(3)
    pos3(motor)
    sleep_ms(3)
    pos3_5(motor)
    sleep_ms(3)
    pos4(motor)
    sleep_ms(3)
    pos4_5(motor)
    sleep_ms(3)

def quarterstep_backward(motor):
    pos4(motor)
    sleep_ms(3)
    pos3(motor)
    sleep_ms(3)
    pos2(motor)
    sleep_ms(3)
    pos1(motor)
    sleep_ms(3)

def fullstep_backward(motor):
    pos4_5(motor)
    sleep_ms(3)
    pos4(motor)
    sleep_ms(3)
    pos3_5(motor)
    sleep_ms(3)
    pos3(motor)
    sleep_ms(3)
    pos2_5(motor)
    sleep_ms(3)
    pos2(motor)
    sleep_ms(3)
    pos1_5(motor)
    sleep_ms(3)
    pos1(motor)
    sleep_ms(3)
    
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