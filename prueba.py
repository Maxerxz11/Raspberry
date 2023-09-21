import adafruit_dht
import time

pin = 4

dht_sensor = adafruit_dht.DHT22(pin)

try:
    while True:

        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        print(temperature)
        print(humidity)

        time.sleep(2)

except KeyboardInterrupt:
    pass

dht_sensor.exit()
