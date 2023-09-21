import time
import adafruit_dht
from board import pin

dht_sensor = adafruit_dht.DHT22(18)

while True:
    temperatura = dht_sensor.temperature  # Variables para leer la temperatura
    print(temperatura)
#    if temperatura is not None:
#        print(f'Temperatura: {temperature:.2f}°C')

#    else:
 #       print("Error[-]")

    time.sleep(1.0)
