# __name__ == '__main__': 代表程式的進入點
import RPi.GPIO as GPIO #RPi.GPIO命名為GPIO
import time
#==function宣告=====================
#def doOneThing(): 
#    i = 10;
#    print("這是doOneThing的i = ",i)
    
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.OUT)
    GPIO.setwarnings(False) 
    #GPIO.output(25,GPIO.HIGH) 

def blink():
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.5)
    
if __name__ == '__main__':
 #   i = 20
 #   print("這是主程式的i = ",i)
 #   doOneThing()
    setup()
    try:
        blink()
    except:
        print('except')
        GPIO.output(25, GPIO.LOW)
    finally:
        GPIO.cleanup()
        print('finally')
        print('synchronize')
   
