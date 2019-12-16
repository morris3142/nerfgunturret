import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
triggerServo = GPIO.PWM(40, 50)
triggerAngle = 3.2
triggerServo.start(triggerAngle)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)

turnServo = GPIO.PWM(33, 50)
angle = 7.5

angle_change = 0.5

def turnLeft(angle):
    for i in range(0, 10):
        angle -= angle_change/10
        if angle < 2.5:
            angle = 2.5
        turnServo.ChangeDutyCycle(angle)
    time.sleep(0.1)
    return angle

def turnRight(angle):
    for i in range(0, 10):
        angle += angle_change/10
        if angle > 12.5:
            angle = 12.5
        turnServo.ChangeDutyCycle(angle)
    time.sleep(0.1)
    return angle

def shoot():
        triggerServo.ChangeDutyCycle(8.4)
        time.sleep(0.3)
        triggerServo.ChangeDutyCycle(3.2)
        time.sleep(0.3)

def startUp():
    turnServo.start(2.5)
    time.sleep(1)
    turnServo.ChangeDutyCycle(12.5)
    time.sleep(1.5)
    turnServo.ChangeDutyCycle(7.5)
    time.sleep(1)

startUp()

try:
    while True:
        buttonLeft = GPIO.input(37)
        buttonRight = GPIO.input(35)
        buttonWarn = GPIO.input(31)
        buttonShoot = GPIO.input(29)
        
        if buttonLeft == False:
            angle = turnLeft(angle)
        elif buttonRight == False:
            angle = turnRight(angle)
        #elif buttonWarn == GPIO.HIGH:
            #warn
        elif buttonShoot == False:
            shoot()
except KeyboardInterrupt:
    GPIO.cleanup()
