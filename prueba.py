import board
import adafruit_dht

pin = board.D4

# Inicializa el sensor
dht_sensor = adafruit_dht.DHT22(pin)

try:
    # Lee la temperatura y la humedad
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity

    print(temperature)
    print(humidity)

except RuntimeError as e:
    print("Error")
