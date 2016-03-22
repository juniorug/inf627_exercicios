#!/usr/bin/env python

import Rpi.GPIO as GPIO
from CharLCD import CharLCD


lcd = CharLCD()
lcd.clear()
lcd.message(" 16x2\n  Standard LCD")
