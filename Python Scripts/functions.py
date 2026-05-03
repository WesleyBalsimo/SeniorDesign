import machine
from machine import Pin
from time import sleep_ms

#global x, y coordinates
coord = [0, 0]

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
    sleep_ms(2)
    pos2(motor)
    sleep_ms(2)
    pos3(motor)
    sleep_ms(2)
    pos4(motor)
    sleep_ms(2)

def fullstep_forward(motor):
    pos1(motor)
    sleep_ms(2)
    pos1_5(motor)
    sleep_ms(2)
    pos2(motor)
    sleep_ms(2)
    pos2_5(motor)
    sleep_ms(2)
    pos3(motor)
    sleep_ms(2)
    pos3_5(motor)
    sleep_ms(2)
    pos4(motor)
    sleep_ms(2)
    pos4_5(motor)
    sleep_ms(2)

def quarterstep_backward(motor):
    pos4(motor)
    sleep_ms(2)
    pos3(motor)
    sleep_ms(2)
    pos2(motor)
    sleep_ms(2)
    pos1(motor)
    sleep_ms(2)

def fullstep_backward(motor):
    pos4_5(motor)
    sleep_ms(2)
    pos4(motor)
    sleep_ms(2)
    pos3_5(motor)
    sleep_ms(2)
    pos3(motor)
    sleep_ms(2)
    pos2_5(motor)
    sleep_ms(2)
    pos2(motor)
    sleep_ms(2)
    pos1_5(motor)
    sleep_ms(2)
    pos1(motor)
    sleep_ms(2)