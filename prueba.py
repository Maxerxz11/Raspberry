import RPi.GPIO as GPIO
import time

# Configura los pines GPIO
RED_PIN = 17
GREEN_PIN = 18
BLUE_PIN = 27

# Configura el modo de los pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Enciende el LED en rojo
GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

# Espera unos segundos
time.sleep(3)

# Apaga el LED
GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

# Limpia los pines GPIO
GPIO.cleanup()
