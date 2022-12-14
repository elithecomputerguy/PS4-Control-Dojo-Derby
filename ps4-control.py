import RPi.GPIO as GPIO

from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

lf = GPIO.PWM(35,100)
lb = GPIO.PWM(36,100)
rf = GPIO.PWM(37,100)
rb = GPIO.PWM(38,100)

speed = 100

class MyController(Controller):
    
    def __int__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        lf.start(speed)
        lb.start(0)
        rf.start(speed)
        rb.start(0)

    def on_down_arrow_press(self):
        rf.start(0)
        rb.start(speed)
        lf.start(0)
        lb.start(speed)

    def on_left_arrow_press(self):
        lf.start(speed)
        lb.start(0)
        rf.start(0)        
        rb.start(speed)

    def on_right_arrow_press(self):
        lf.start(0)
        lb.start(speed)
        rf.start(speed)
        rb.start(0)

    def on_x_press(self):
        lf.start(0)
        lb.start(0)
        rf.start(0)
        rb.start(0)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
