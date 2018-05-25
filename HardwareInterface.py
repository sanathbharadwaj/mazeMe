
import time
import RPi.GPIO as GPIO

dd = HardwareInterface()
dd.moveForward()


class HardwareInterface:

	def __init__(self):
		self.m1p1 = 36
		self.m1p2 = 38
		self.m2p1 = 31
		self.m2p2 = 33
		self.t = []
		self.e = []
		self.rotation = 0;
		self.t[0] = 3
		self.e[0] = 5
		self.t[1] = 3
		self.e[1] = 5
		self.t[2] = 3
		self.e[2] = 5
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(m1p1, GPIO.OUT)
		GPIO.setup(m1p2, GPIO.OUT)
		GPIO.setup(m2p1, GPIO.OUT)
		GPIO.setup(m2p2, GPIO.OUT)

		GPIO.setup(t[0],GPIO.OUT)
		GPIO.setup(e[0] ,GPIO.IN)

		GPIO.setup(t[1] ,GPIO.OUT)
		GPIO.setup(e[1] ,GPIO.IN)

		GPIO.setup(t[2] ,GPIO.OUT)
		GPIO.setup(e[2] ,GPIO.IN)

	def moveForward():
		GPIO.output(m1p1, True)
		GPIO.output(m1p2, False)
		GPIO.output(m2p1, True)
		GPIO.output(m2p2, False)
		time.sleep(0.3)
		GPIO.output(m1p1, False)
		GPIO.output(m1p2, False)
		GPIO.output(m2p1, False)
		GPIO.output(m2p2, False)

	def moveBackward():
		GPIO.output(m1p1, False)
		GPIO.output(m1p2, True)
		GPIO.output(m2p1, False)
		GPIO.output(m2p2, True)
		time.sleep(0.3)
		GPIO.output(m1p1, False)
		GPIO.output(m1p2, False)
		GPIO.output(m2p1, False)
		GPIO.output(m2p2, False)


	def turn(direction):
		if direction == 1:
			GPIO.output(m1p1, True)
			GPIO.output(m1p2, False)
			GPIO.output(m2p1, False)
			GPIO.output(m2p2, False)
			time.sleep(0.3)
			GPIO.output(m1p1, False)
			GPIO.output(m1p2, False)
			GPIO.output(m2p1, False)	
			GPIO.output(m2p2, False)
		else:
			GPIO.output(m1p1, False)
			GPIO.output(m1p2, False)
			GPIO.output(m2p1, True)
			GPIO.output(m2p2, False)
			time.sleep(0.3)
			GPIO.output(m1p1, False)
			GPIO.output(m1p2, False)
			GPIO.output(m2p1, False)
			GPIO.output(m2p2, False)


	def getSensor(i):
		maxDistance = 40;
		GPIO.output(t[i], True)
    	time.sleep(0.00001)
    	GPIO.output(t[i], False)
    	start = time.time()

    	while GPIO.input(e[i])==0:
        	start = time.time()

    	while GPIO.input(e[i])==1:
        	stop = time.time()

    	# Calculate pulse length
    	elapsed = stop-start

    	# Distance pulse travelled in that time is time
    	# multiplied by the speed of sound (cm/s)
    	distance = elapsed * 34300

    	# That was the distance there and back so halve the value
    	distance = distance / 2

    	if distance > maxDistance:
    		distance = maxDistance

    	nValue = (maxDistance - distance)/maxDistance

    	return nValue

    def getRotation():
    	return rotation


	


