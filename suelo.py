import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin_main = 17

GPIO.setup(pin_main, GPIO.IN)  # GPIO.IN declaro que se un pin de entrada

while True:

    datos = GPIO.input(pin_main)  # con este input leeo los datos del pin

    if datos == 0:
        print(f"{datos} la planta esta muy seca")

    elif datos == 1:
        print(f"{datos} la planta esta humeda")

    time.sleep(1.0)
