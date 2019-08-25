from Tkinter import *
import RPi.GPIO as GPIO
import time
import sys


dutyR = 15.5
dutyL = 10.5
duty0 = 14.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(2.5)

def rot(deg):
	if deg > 0:
		pwm.ChangeDutyCycle(dutyL)
		# 0.05s = 360 deg
                slp_time = (float(deg)/360.0)*0.05
                time.sleep(slp_time)
		pwm.ChangeDutyCycle(duty0)

# class App:
# 	
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         scale = Scale(frame, from_=100, to=130, 
#               orient=HORIZONTAL, command=self.update)
#         scale.grid(row=0)
# 
# 
#     def update(self, angle):
#         duty = float(angle) / 10.0 + 2.5
#         pwm.ChangeDutyCycle(duty)
# 
# root = Tk()
# root.wm_title('Servo Control')
# app = App(root)
# root.geometry("200x50+0+0")
# root.mainloop()

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: angle'
        sys.exit(1)
    
    angle = args[0]
    rot(angle)
    GPIO.cleanup()
    exit(1)

if __name__ == '__main__':
    main()

