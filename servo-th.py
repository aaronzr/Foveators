from Tkinter import *
import RPi.GPIO as GPIO
import time

pin1 = 18
pin2 = 17
pwm_stall = 115.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
pwm1 = GPIO.PWM(pin1, 100)
pwm2 = GPIO.PWM(pin2, 100)
pwm1.start(2.5)
pwm2.start(2.5)

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=-10, to=10, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty1 = (float(angle) + pwm_stall) / 10.0 + 2.5
        duty2 = (float(angle) + pwm_stall) / 10.0 + 2.5
        pwm1.ChangeDutyCycle(duty1)
        pwm2.ChangeDutyCycle(duty2)

root = Tk()
root.wm_title('THETA')
app = App(root)
root.geometry("220x50+0+0")
root.mainloop()
