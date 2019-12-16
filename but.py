import RPi.GPIO as GPIO
from gpiozero import Button
import time

GPIO.setup(33, GPIO.OUT)
turnServo = GPIO.PWM(33, 50)
right = Button(26)
left = Button(19)

angle = 7.5

def turnLeft(angle):
    angle -= .5
    if angle < 2.5:
        angle = 2.5
    turnServo.ChangeDutyCycle(angle)
    time.sleep(0.3)
    return angle

def turnRight(angle):
    angle += .5
    if angle > 12.5:
        angle = 12.5
    turnServo.ChangeDutyCycle(angle)
    time.sleep(0.3)
    return angle

def startUp():
    turnServo.start(2.5)
    time.sleep(0.3)
    turnServo.ChangeDutyCycle(12.5)
    time.sleep(0.3)
    turnServo.ChangeDutyCycle(7.5)
    time.sleep(0.3)

startUp()

try:
    while True:
        if right.is_pressed:
            angle = turnRight(angle)
        elif left.is_pressed:
            angle = turnLeft(angle)

except KeyboardInterrupt:
    GPIO.cleanup
