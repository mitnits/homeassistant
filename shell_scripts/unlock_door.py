#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN=4

GPIO.setup(PIN,  GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)
GPIO.output(PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(PIN, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(PIN, GPIO.HIGH)


GPIO.cleanup(PIN)
