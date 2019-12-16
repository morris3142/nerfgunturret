import RPi.GPIO as GPIO
import serial, time, sys
from pygame import mixer

mixer.init()
sound = mixer.Sound("Turret_sp_sabotage_factory_good_prerange01.wav")

ser = serial.Serial(sys.argv[1],9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnLeft():
    print("turn left")
    ser.write(bytes([65]))
    time.sleep(0.1)
    
def turnRight():
    print("turn right")
    ser.write(bytes([66]))    
    time.sleep(0.1)
    
def shoot():
    print("shoot")
    ser.write(bytes([67]))    
    time.sleep(0.4)

def warn(sound):
    sound.play(1)
    time.sleep(2)

playing = False
try:
    while True:
        buttonLeft = GPIO.input(37)
        buttonRight = GPIO.input(35)
        buttonWarn = GPIO.input(31)
        buttonShoot = GPIO.input(29)
        
        if buttonLeft == False:
            turnLeft()
        elif buttonRight == False:
            turnRight()
        elif buttonWarn == False and playing == False:
            playing = True
            warn(sound)
            playing = False
        elif buttonShoot == False:
            shoot()
except KeyboardInterrupt:
    GPIO.cleanup()
        
