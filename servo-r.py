from Tkinter import *
import RPi.GPIO as GPIO
import time

pin1 = 18
pin2 = 17
pwm_stall = 115.0 / 10 + 2.5
pwmR = 100.0 / 10 + 2.5
pwmL = 130.0 / 10 + 2.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
pwm1 = GPIO.PWM(pin1, 100)
pwm2 = GPIO.PWM(pin2, 100)
pwm1.start(2.5)
pwm2.start(2.5)


def minusR():
    duty1 = pwmR
    duty2 = pwmL
    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)
    print 'r-'

def plusR():
    duty1 = pwmL
    duty2 = pwmR
    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)
    print 'r+'

def stall():
    duty1 = pwm_stall
    duty2 = pwm_stall
    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)
    print '0'

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=-10, to=10, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        print angle
        if angle < -5:
            #minusR()
            print 'r-'
        if angle > 5:
            #plusR()
            print'r+'
        else:
           #stall()
           print '0'


root = Tk()
root.wm_title('R')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
