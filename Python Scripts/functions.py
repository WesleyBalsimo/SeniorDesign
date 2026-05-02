from machine import Pin
from time import sleep_ms

# Motor output
pin0 = machine.Pin(0, Pin.OUT)
pin1 = machine.Pin(1, Pin.OUT)
pin2 = machine.Pin(2, Pin.OUT)
pin3 = machine.Pin(3, Pin.OUT)

def pos1():
    pin0.value(0)
    pin1.value(0)
    pin2.value(0)
    pin3.value(1)

def pos1_5():
    pin0.value(0)
    pin1.value(0)
    pin2.value(1)
    pin3.value(1)   

def pos2():
    pin0.value(0)
    pin1.value(0)
    pin2.value(1)
    pin3.value(0)

def pos2_5():
    pin0.value(0)
    pin1.value(1)
    pin2.value(1)
    pin3.value(0)

def pos3():
    pin0.value(0)
    pin1.value(1)
    pin2.value(0)
    pin3.value(0)

def pos3_5():
    pin0.value(1)
    pin1.value(1)
    pin2.value(0)
    pin3.value(0)

def pos4():
    pin0.value(1)
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)

def pos4_5():
    pin0.value(1)
    pin1.value(0)
    pin2.value(0)
    pin3.value(1)

def sleep():
    pin0.value(0)
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)

def fullstep_forward():
    pos1()
    sleep_ms(3)
    pos2()
    sleep_ms(3)
    pos3()
    sleep_ms(3)
    pos4()
    sleep()

def halfstep_forward():
    pos1()
    sleep_ms(3)
    pos1_5()
    sleep_ms(3)
    pos2()
    sleep_ms(3)
    pos2_5()
    sleep_ms(3)
    pos3()
    sleep_ms(3)
    pos3_5()
    sleep_ms(3)
    pos4()
    sleep_ms(3)
    pos4_5()
    sleep()

def fullstep_backward():
    pos4()
    sleep_ms(3)
    pos3()
    sleep_ms(3)
    pos2()
    sleep_ms(3)
    pos1()
    sleep_ms(3)

def halfstep_backward():
    pos4_5()
    sleep_ms(3)
    pos4()
    sleep_ms(3)
    pos3_5()
    sleep_ms(3)
    pos3()
    sleep_ms(3)
    pos2_5()
    sleep_ms(3)
    pos2()
    sleep_ms(3)
    pos1_5()
    sleep_ms(3)
    pos1()
    sleep()