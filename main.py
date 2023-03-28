#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.display import FbMem

screen = FbMem()

m = LargeMotor(OUTPUT_A)


screen.draw.rectangle((10,10,60,20), fill='black')

while True:
    m.on_for_rotations(SpeedPercent(100), 1)
    m.on_for_rotations(SpeedPercent(100), -1)
