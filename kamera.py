import RPi.GPIO as GPIO
import picamera
import time
camera = picamera.PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Czujnik Ruchu 
GPIO.setup(5, GPIO.OUT)         #Dioda LED
j=0;

while True:
       i=GPIO.input(11)
       if i==0:                 #Gdy czujnik nie wykryje ruchu 
             print "Brak ruchu",i
             GPIO.output(5, 0)  #Turn OFF LED
             time.sleep(0.5)
       elif i==1:               #Gdy czujnik wykryje ruch 
             print "Wykryto ruch",i
             GPIO.output(5, 1)  #Zapalanie diody LED 
             j=j+1
             camera.capture('image%05d.jpg'%j) #zrobienie zdjecia 
	     time.sleep(0.5)
