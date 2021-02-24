import RPi.GPIO as GPIO
import time
import picamera
import datetime as dt

camera = picamera.PiCamera()
#camera.vflip = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
start = 0 
end = 0
TRIG = 4
ECHO = 18
BUTTON2 = 9
BUTTON = 11
GREEN = 17
YELLOW = 27
RED = 22
BUZZER = 21

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUTTON2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)


def green_light():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)

def yellow_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)
    

def get_distance():

    global end
    global start
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = round(sig_time / 0.000058, 2)



    return distance


camera.annotate_background = True
camera.resolution = (1920, 1080)
camera.brightness = 60
camera.contrast = 60
camera.annotate_text_size = 70

val = 0
try:
    
   
    while True:
        button_state = GPIO.input(BUTTON)
        
        if button_state == False:
            
            val = 1
            camera.start_preview()
        while val == 1:
            camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S           DISTANCE: ') + (str(get_distance())) + (' [cm]')
            distance = get_distance()
            time.sleep(0.15)
            print(distance)

            if distance >= 20:
                green_light()
            elif 20 > distance > 10:
                yellow_light()
            elif distance <= 10:
                red_light()
            elif distance <= 11:
                GPIO.output(BUZZER, 1)
            
           
except:
    camera.stop_preview()
    GPIO.cleanup()
