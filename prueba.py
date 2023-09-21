import time
import board
import adafruit_dht


sensor = adafruit_dht.DHT22(board.D4)

while True:
    temperature = dht_device.temperature  # Variables para leer la temperatura

    if temperature is not None:
        print(temperature)

    else:
        print("Error[-]")

    time.sleep(1.0)
