from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4)

while True:
    print(f'Distancia: {sensor.distance * 100:.2f} cm')
    sleep(1)
