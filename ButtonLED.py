from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(26)

i = 0

while True:
	if button.is_pressed:
		led.on()
		sleep(0.1)
	else:
		led.off()