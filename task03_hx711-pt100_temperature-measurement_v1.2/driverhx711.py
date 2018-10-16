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

class Thermometer:
#利用电阻温度变化关系，生成函数；读取电阻值，返回温度（℃）
    def read(self,x):
        A = -2.0368457321432898e-07
        B = 0.0011559161342576463
        C = 2.3291910528129707 
        D = -244.24493259931052
        T = A*x*x*x + B*x*x + C*x + D
        return T

class ResMeasure:
#利用电阻电压变化关系，生成函数；读取电阻值，返回电阻（Ω）
    def get_res(self,x):
        A = 7.662896731735825e-06
        B = -0.004338996810832222
        C = -0.6663393866185219
        D = 309.8867433810022
        r = A*x*x*x + B*x*x + C*x + D
        return r
