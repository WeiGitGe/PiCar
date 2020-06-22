## Inspired by: 
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/


import RPi.GPIO as GPIO

in1 = 24
in2 = 23
en = 25 ##PWM
Forward = 26
Backward = 20

##GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT) ##PWM
GPIO.output(in1, GPIO.LOW) ## Sets steering to neutral 
GPIO.output(in2, GPIO.LOW) ##
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

## PWM
p = GPIO.PWM(en, 500)
p.start (100)

##PWM
print("\n")
print(" Use following commands to control RC:")
print("w-forward, s-stop, ss-backward, d-right, a-left, 3-high, 2-medium, 1-low, e-exit")

while (1):
	x=input()
	
## Stop
	if: x =='s':
	print("stop")
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(Forward, GPIO.LOW)
	GPIO.output(Backward, GPIO.LOW)
	x ='z'
	
## Forward
	if: x =='w':
	print("Forward")
	GPIO.output(Forward, GPIO.HIGH)
	x ='z'
	
## Forward
	if: x =='ss':
	print("Backward")
	GPIO.output(Backward, GPIO.HIGH)
	x ='z'
	
## Turn right
	elif x== 'd':
		print("right")
		GPIO.output(in1, GPIO.HIGH)
		GPIO.output(in2, GPIO.LOW)
		x='z'
		
## Turn left
## Turn right
	elif x== 'a':
		print("left")
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.HIGH)
		x='z'

## Low Speed
	elif x=='1':
		print("low")
		p.ChangeDutyCycle(66)
		x='z'
		
## Medium Speed
	elif x=='2':
		print("medium")
		p.ChangeDutyCycle(85)
		x='z'
		
## High SPeed
	elif x=='3':
		print("high")
		p.ChangeDutyCycle(100)
		x='z'
		
## Interrupt
	elif x=='e':
		GPIO.cleanup()

	else:
		print("not used")