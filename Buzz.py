#!/usr/bin/env python3
########################################################################
# Filename    : Doorbell.py
# Description : Make doorbell with buzzer and button
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

buzzerPin = 13    # define buzzerPin

def setupbuzz():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(buzzerPin, GPIO.OUT)   # set buzzerPin to OUTPUT mode

def loopbuzz():
    for i in range(0,5):
        GPIO.output(buzzerPin,GPIO.HIGH) # turn on buzzer
        print ('buzzer turned on >>>')
        time.sleep(1)
        GPIO.output(buzzerPin,GPIO.LOW) # turn off buzzer
        print ('buzzer turned off <<<')
        time.sleep(1)

def buzz():
    try: 
        setupbuzz()
        loopbuzz()
        destroy()
    except:
        destroy()

