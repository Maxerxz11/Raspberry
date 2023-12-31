import time
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


sensor = Adafruit_DHT.DHT22
sensor_pin = 4
i = 0
RED_PIN = 17
GREEN_PIN = 18
BLUE_PIN = 27
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

while i < 100:
    # LO que hago aca es declarar una varible de temperatura para sacar analizar con el sencor la funcion read es para leer sus datos
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, sensor_pin)

    if temperatura is not None and temperatura > 20:
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)

        print(f'Temperatura: {temperatura:.2f}°C')
        print("----------------------------------------------")
        print(f'Humedad: {humedad:.2f}%')
        print("----------------------------------------------")
        i = i + 1

    elif temperatura is not None and temperatura < 20:
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)

        GPIO.output(BLUE_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)

        print(f'Temperatura: {temperatura:.2f}°C')
        print("----------------------------------------------")
        print(f'Humedad: {humedad:.2f}%')
        print("----------------------------------------------")
        i = i + 1
    time.sleep(2.0)

GPIO.cleanup()
