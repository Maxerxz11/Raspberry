import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin = 18

# EL pin tiene que ser en out porque el buzer libera el sonido
GPIO.setup(pin, GPIO.OUT)


while True:
    # Prender
    GPIO.output(pin, GPIO.HIGH)

    time.sleep(1)
