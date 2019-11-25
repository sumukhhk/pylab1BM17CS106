import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
user_tags=['']
customer_tags=['']
def servo_motor():  
    servoPIN = 17
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) 
    p.start(2.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    p.stop()


def rfid_door():
    
    ser = serial.Serial ("/dev/ttyAMA0")                            
    ser.baudrate = 9600                                            
    data = ser.read(12)
    if data in customer_tags:
        print("Welcome to XYZ Shopping Mart!!!\n")
        servo_motor()
    ser.close ()

#def 
servo_motor()
