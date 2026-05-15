import machine
from machine import Pin, bitstream
from time import sleep

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

#limit switch input pins
pinLimit_x = machine.Pin(28, Pin.IN, machine.Pin.PULL_UP)
pinLimit_y = machine.Pin(29, Pin.IN, machine.Pin.PULL_UP)

# pinLimitPullUp_x = machine.Pin(26, Pin.OUT)
# pinLimitPullUp_y = machine.Pin(27, Pin.OUT)
# pinLimitPullUp_x.value(1)
# pinLimitPullUp_y.value(1)

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

<<<<<<< HEAD
def mSleep(motor):
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(0)
=======
#def sleep(motor):
#    motor[0].value(0)
#    motor[1].value(0)
#    motor[2].value(0)
#    motor[3].value(0)
>>>>>>> 8d59dcb2e888be2b564416336eb0ae013b69ac0e

#define movement functions for full step and half step sequences
def fullstep_forward(motor):
    pos1(motor)
    sleep(3 / 1_000)
    pos2(motor)
    sleep(3 / 1_000)
    pos3(motor)
    sleep(3 / 1_000)
    pos4(motor)
    sleep(3 / 1_000)

def halfstep_forward(motor):
    pos1(motor)
    sleep(3 / 1_000)
    pos1_5(motor)
    sleep(3 / 1_000)
    pos2(motor)
    sleep(3 / 1_000)
    pos2_5(motor)
    sleep(3 / 1_000)
    pos3(motor)
    sleep(3 / 1_000)
    pos3_5(motor)
    sleep(3 / 1_000)
    pos4(motor)
    sleep(3 / 1_000)
    pos4_5(motor)
    sleep(3 / 1_000)

def fullstep_backward(motor):
    pos4(motor)
    sleep(3 / 1_000)
    pos3(motor)
    sleep(3 / 1_000)
    pos2(motor)
    sleep(3 / 1_000)
    pos1(motor)
    sleep(3 / 1_000)

def halfstep_backward(motor):
    pos4_5(motor)
    sleep(3 / 1_000)
    pos4(motor)
    sleep(3 / 1_000)
    pos3_5(motor)
    sleep(3 / 1_000)
    pos3(motor)
    sleep(3 / 1_000)
    pos2_5(motor)
    sleep(3 / 1_000)
    pos2(motor)
    sleep(3 / 1_000)
    pos1_5(motor)
    sleep(3 / 1_000)
    pos1(motor)
    sleep(3 / 1_000)
    

#This function doesnt really work at the moment
def boardlight(x):
    timing = [300, 900, 700, 500]
    np = Pin(16, Pin.OUT)
    red = bytearray([0,20,0])
    green = bytearray([20,0,0])
    blue = bytearray([0,0,20])
    while(x == 1):
        bitstream(np, 0, timing, red)
        sleep(1.0)
        bitstream(np, 0, timing, green)
        sleep(1.0)
        bitstream(np, 0, timing, blue)
<<<<<<< HEAD
        sleep(1.0)
=======
        sleep_ms(1000)
>>>>>>> 8d59dcb2e888be2b564416336eb0ae013b69ac0e
