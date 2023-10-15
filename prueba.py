import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

red = 17
green = 23
blue = 22

sensor = Adafruit_DHT.DHT22
pin = 4

while True:
    # LO que hago aca es declarar una varible de temperatura para sacar analizar con el sencor la funcion read es para leer sus datos
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    if temperatura is not None and temperatura > 18:
        GPIO.setup(red, GPIO.OUT)

        print(f'Temperatura: {temperatura:.2f}°C')
        print("----------------------------------------------")
        print(f'Humedad: {humedad:.2f}%')
        print("----------------------------------------------")

    elif temperatura is not None and temperatura < 18:
        GPIO.setup(blue, GPIO.OUT)

        print(f'Temperatura: {temperatura:.2f}°C')
        print("----------------------------------------------")
        print(f'Humedad: {humedad:.2f}%')
        print("----------------------------------------------")

    else:
        print("Error[-]")
    time.sleep(2.0)
