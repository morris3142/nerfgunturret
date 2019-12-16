from gpiozero import LED, Button, Servo
from signal import pause
import time

led = LED(17)
left = Button(26)
right = Button(19)
butThree = Button(6)
butFour = Button(5)
servo = Servo(13)

def turnLeft():
	value = servo.value
	val_change = 0.3
	for i in range(0, 10):
		value += val_change/10
		if (value > 1):
			servo.max()
		else:
			servo.value = value
		time.sleep(0.01)
	print(servo.value)

def turnRight():
	value = servo.value
	val_change = 0.3
	for i in range(0, 10):
		value -= val_change/10
		if (value < -1):
			servo.min()
		else:
			servo.value = value
		time.sleep(0.01)
	print(servo.value)

def startUp():
	servo.max()
	time.sleep(1)
	servo.min()
	time.sleep(1)
	servo.mid()

#startUp()

#prev_val = 0
while True:
#	val = servo.value
#	if val != prev_val:
#		print(servo.value)
#	prev_val = val
	if left.is_pressed:
		led.on()
		turnLeft()
	elif right.is_pressed:
		turnRight()
	elif butThree.is_pressed:
		print("THREE")
	elif butFour.is_pressed:
		print("FOUR")
	else:
		led.off()
