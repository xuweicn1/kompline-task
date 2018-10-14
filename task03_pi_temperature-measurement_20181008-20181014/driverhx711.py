import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class HX711:
    def __init__(self, SCK, DT):
        GPIO.setup(DT, GPIO.IN)
        GPIO.setup(SCK, GPIO.OUT, initial=0)
        self.DT = DT
        self.SCK = SCK

    def getdv(self):
        d = 0
        while GPIO.input(self.DT)==1:
            pass
        for i in range(24):
            GPIO.output(self.SCK, 1)
            GPIO.output(self.SCK, 0)
            d= d<<1 | GPIO.input(self.DT)
        GPIO.output(self.SCK, 1)
        GPIO.output(self.SCK, 0)
        return d