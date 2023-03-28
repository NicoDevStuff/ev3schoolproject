#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound


m = LargeMotor(OUTPUT_A)

while True:
    m.on_for_rotations(SpeedPercent(100), 1)
    m.on_for_rotations(SpeedPercent(100), -1)
