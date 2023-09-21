import time
import board
import adafruit_dht


sensor = adafruit_dht.DHT22(board.D4)

while True:
    temperatura = sensor.temperatura  # Variables para leer la temperatura

    if temperatura is not None:
        print(temperatura)

    else:
        print("Error[-]")

    time.sleep(1.0)
