#!/usr/bin/env python

import RPi.GPIO as GPIO
from CharLCD import CharLCD


lcd = CharLCD()
lcd.begin(16, 1)
lcd.clear()
lcd.message(" 16x2\n  Standard LCD")
