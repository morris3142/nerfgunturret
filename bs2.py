import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
p = GPIO.PWM(33, 50)
angle = 3.2
p.start(angle)

def shoot():
        p.ChangeDutyCycle(8.4)
        time.sleep(0.3)
        p.ChangeDutyCycle(3.2)
        time.sleep(0.3)

def turnLeft(angle):
        print(angle)
        angle = 3.2
        p.ChangeDutyCycle(angle)
        return angle

def turnRight(angle):
        print(angle)
        angle = 8.4
        p.ChangeDutyCycle(angle)
        return angle

try:
	while True:
                shoot()
#                time.sleep(0.5)
#                angle = turnLeft(angle)
#                time.sleep(0.5)
#                angle = turnRight(angle)
#                time.sleep(0.5)
#		p.ChangeDutyCycle(7.5)
#		time.sleep(1)
#		p.ChangeDutyCycle(12.5)
#		time.sleep(1)
#		p.ChangeDutyCycle(2.5)
#		time.sleep(1)

except KeyboardInterrupt:
        angle = 3.2
        p.ChangeDutyCycle(3.2)
        p.stop()
        GPIO.cleanup()
        print(angle)
