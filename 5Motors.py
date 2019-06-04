

# Importing Libraries

import RPi.GPIO as GPIO
import time
from Tkinter import *
#import Tkinter.font

# Libraries Imported successfully

# Raspberry Pi 3 Pin Settings

PWMPin = 11 # PWM Pin connected to ENA.
Motor1A = 16 # Connected to Input 1.
Motor1B = 18 # Connected to Input 2.
PWMPin2 = 36 #Motor 2
Motor2A = 38
Motor2B = 40
PWMPin3 = 29#Motor 3
Motor3A = 31 
Motor3B = 33
PWMPin4 = 32 #Motor 4
Motor4A = 35
Motor4B = 37
PWMPin5 = 22 #Motor 5
Motor5A = 24
Motor5B = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location

GPIO.setup(PWMPin, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
############################
GPIO.setup(PWMPin2, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
############################
GPIO.setup(PWMPin3, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor3A, GPIO.OUT)
GPIO.setup(Motor3B, GPIO.OUT)
############################
GPIO.setup(PWMPin4, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor4A, GPIO.OUT)
GPIO.setup(Motor4B, GPIO.OUT)
############################
GPIO.setup(PWMPin5, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor5A, GPIO.OUT)
GPIO.setup(Motor5B, GPIO.OUT)

#Now set the start speed to be LOW

GPIO.output(PWMPin, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.LOW)
#############################
GPIO.output(PWMPin2, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor2A, GPIO.LOW)
GPIO.output(Motor2B, GPIO.LOW)
#############################
GPIO.output(PWMPin3, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor3A, GPIO.LOW)
GPIO.output(Motor3B, GPIO.LOW)
#############################
GPIO.output(PWMPin4, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor4A, GPIO.LOW)
GPIO.output(Motor4B, GPIO.LOW)
#############################
GPIO.output(PWMPin5, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor5A, GPIO.LOW)
GPIO.output(Motor5B, GPIO.LOW)



PwmValue = GPIO.PWM(PWMPin, 255) # We have set our PWM frequency to 2000.
PwmValue2 = GPIO.PWM(PWMPin2, 255) # We have set our PWM frequency to 2000.
PwmValue3 = GPIO.PWM(PWMPin3, 255) # We have set our PWM frequency to 2000.
PwmValue4 = GPIO.PWM(PWMPin4, 255) # We have set our PWM frequency to 2000.
PwmValue5 = GPIO.PWM(PWMPin5, 255) # We have set our PWM frequency to 2000.
PwmValue.start(40) # That's the maximum value 100 %.
PwmValue2.start(40) # That's the maximum value 100 %.
PwmValue3.start(40) # That's the maximum value 100 %.
PwmValue4.start(40) # That's the maximum value 100 %.
PwmValue5.start(40) # That's the maximum value 100 %.

# Raspberry Pi 3 Pin Settings Completed

# tkinter GUI basic settings

Gui = Tk()
Gui.title("Spinfinity")
Gui.config(background= "grey1")
Gui.minsize(800,400)
#Font1 = tkinter.font.Font(family = 'Helvetica', size = 18, weight = 'bold')

# tkinter simple GUI created

def Motor1Clockwise():
    GPIO.output(Motor1A, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor1B, GPIO.HIGH)
    
def Motor1AntiClockwise():
    GPIO.output(Motor1A, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor1B, GPIO.LOW)

def Motor1Stop():
    GPIO.output(Motor1A, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor1B, GPIO.LOW)
    
def ChangePWM(self):
    PwmValue.ChangeDutyCycle(Scale1.get())
####
def Motor2Clockwise():
    GPIO.output(Motor2A, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor2B, GPIO.HIGH)
    
def Motor2AntiClockwise():
    GPIO.output(Motor2A, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor2B, GPIO.LOW)

def Motor2Stop():
    GPIO.output(Motor2A, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor2B, GPIO.LOW)
    
def ChangePWM2(self):
    PwmValue2.ChangeDutyCycle(Scale2.get())
####
def Motor3Clockwise():
    GPIO.output(Motor3A, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor3B, GPIO.HIGH)
    
def Motor3AntiClockwise():
    GPIO.output(Motor3A, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor3B, GPIO.LOW)

def Motor3Stop():
    GPIO.output(Motor3A, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor3B, GPIO.LOW)
    
def ChangePWM3(self):
    PwmValue3.ChangeDutyCycle(Scale3.get())
####
def Motor4Clockwise():
    GPIO.output(Motor4A, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor4B, GPIO.HIGH)
    
def Motor4AntiClockwise():
    GPIO.output(Motor4A, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor4B, GPIO.LOW)

def Motor4Stop():
    GPIO.output(Motor4A, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor4B, GPIO.LOW)
    
def ChangePWM4(self):
    PwmValue4.ChangeDutyCycle(Scale4.get())
####
def Motor5Clockwise():
    GPIO.output(Motor5A, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor5B, GPIO.HIGH)
    
def Motor5AntiClockwise():
    GPIO.output(Motor5A, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor5B, GPIO.LOW)

def Motor5Stop():
    GPIO.output(Motor5A, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor5B, GPIO.LOW)
    
def ChangePWM5(self):
    PwmValue5.ChangeDutyCycle(Scale5.get())
	
	#########################
	
	

Button1 = Button(Gui, text='Clockwise Motor 1', command = Motor1Clockwise, bg='green2', height = 2, width = 15)
Button1.grid(row=1,column=0)

Button3 = Button(Gui, text='Counter Clockwise 1', command = Motor1AntiClockwise, bg='deep sky blue', padx = 30, height = 2, width = 10)
Button3.grid(row=1,column=1)

Button2 = Button(Gui, text=' Motor 1 Stop', command = Motor1Stop, bg='red', height = 2, width = 10)
Button2.grid(row=1,column=2)

Text3 = Label(Gui,text='Motor 1 RPM', bg = 'grey1', fg='#FFFFFF', height = 2, width = 10)#, padx = 10, pady = 10)
Text3.grid(row=2,columnspan=1)

Scale1 = Scale(Gui, from_=40, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM, length=250, width=20)
Scale1.grid(row=2,column=1, columnspan=3)

########################################

Button4 = Button(Gui, text='Clockwise Motor 2', command = Motor2Clockwise, bg='green2', height = 2, width = 15)
Button4.grid(row=3,column=0)

Button5 = Button(Gui, text=' Motor Stop', command = Motor2Stop, bg='red', height = 2, width = 10)
Button5.grid(row=3,column=2)

Button6 = Button(Gui, text='Counter Clockwise2', command = Motor2AntiClockwise, bg='deep sky blue', padx = 30, height = 2, width = 10)
Button6.grid(row=3,column=1)

Text4 = Label(Gui,text='Motor 2 RPM', bg = 'grey1', fg='#FFFFFF', height = 2, width = 10) #padx = 10, pady = 10)
Text4.grid(row=4,columnspan=1)

Scale2 = Scale(Gui, from_=40, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM2, length=250, width=20)
Scale2.grid(row=4,column=1, columnspan=3)

########################################

Button7 = Button(Gui, text='Clockwise Motor 3', command = Motor3Clockwise, bg='green2', height = 2, width = 15)
Button7.grid(row=5,column=0)

Button8 = Button(Gui, text=' Motor Stop', command = Motor3Stop, bg='red', height = 2, width = 10)
Button8.grid(row=5,column=2)

Button9 = Button(Gui, text='Counter Clockwise3', command = Motor3AntiClockwise, bg='deep sky blue', padx = 30, height = 2, width = 10)
Button9.grid(row=5,column=1)

Text5 = Label(Gui,text='Motor 3 RPM', bg = 'grey1', fg='#FFFFFF', height = 2, width = 10) #padx = 10, pady = 10)
Text5.grid(row=6,columnspan=1)

Scale3 = Scale(Gui, from_=40, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM3, length=250, width=20)
Scale3.grid(row=6,column=1, columnspan=3)

########################################

Button10 = Button(Gui, text='Clockwise Motor 4', command = Motor4Clockwise, bg='green2', height = 2, width = 15)
Button10.grid(row=7,column=0)

Button11 = Button(Gui, text=' Motor Stop', command = Motor4Stop, bg='red', height = 2, width = 10)
Button11.grid(row=7,column=2)

Button12 = Button(Gui, text='Counter Clockwise4', command = Motor4AntiClockwise, bg='deep sky blue', padx = 30, height = 2, width = 10)
Button12.grid(row=7,column=1)

Text6 = Label(Gui,text='Motor 4 RPM', bg = 'grey1', fg='#FFFFFF', height = 2, width = 10) #padx = 10, pady = 10)
Text6.grid(row=8,columnspan=1)

Scale4 = Scale(Gui, from_=40, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM4, length=250, width=20)
Scale4.grid(row=8,column=1, columnspan=3)

########################################

Button13 = Button(Gui, text='Clockwise Motor 5', command = Motor5Clockwise, bg='green2', height = 2, width = 15)
Button13.grid(row=1,column=4)

Button14 = Button(Gui, text=' Motor Stop', command = Motor5Stop, bg='red', height = 2, width = 10)
Button14.grid(row=1,column=5)

Button15 = Button(Gui, text='Counter Clockwise5', command = Motor5AntiClockwise, bg='deep sky blue', padx = 30, height = 2, width = 10)
Button15.grid(row=1,column=6)

Text7 = Label(Gui,text='Motor 5 RPM', bg = 'grey1', fg='#FFFFFF', height = 2, width = 10) #padx = 10, pady = 10)
Text7.grid(row=2, column=4,columnspan=1)

Scale5 = Scale(Gui, from_=40, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM5, length=250, width=20)
Scale5.grid(row=2,column=5, columnspan=3)


Gui.mainloop()
