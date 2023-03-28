from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
# import pygame
import sys

# pygame.init()
# screen = pygame.display.set_mode((0, 0 ), pygame.FULLSCREEN)
# clock = pygame.time.Clock()

whl = LargeMotor(OUTPUT_A) # Left driving motor
whr = LargeMotor(OUTPUT_D) # Right driving motor
rom = MediumMotor(OUTPUT_B) # Rotating motor
dst = UltrasonicSensor()

x = 0
y = 0
dt = 0

positions = []

while True:
    # screen.fill((0, 0, 0))

    # dt = clock.tick(0)
    
    # pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50));
    
    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_RIGHT]:
    #     x += 0.21 * dt
    # if keys[pygame.K_LEFT]:
    #     x -= 0.21 * dt
    # if keys[pygame.K_UP]:
    #     y -= 0.21 * dt
    # if keys[pygame.K_DOWN]:
    #     y += 0.21 * dt

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit(1)


    # pygame.display.update()

    rom.on_for_rotations(SpeedPercent(100), 1)
    rom.on_for_rotations(SpeedPercent(100), -1)

