import time
import board
import adafruit_dht

pin = board.D8

dht_sensor = adafruit_dht.DHT22(pin)

while True:
    temperatura = dht_sensor.temperature  # Variables para leer la temperatura

    if temperatura is not None:
        print(f'Temperatura: {temperature:.2f}°C')

    else:
        print("Error[-]")

    time.sleep(1.0)
