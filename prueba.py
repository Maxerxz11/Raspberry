import board
import adafruit_dht

pin = board.D4

# Inicializa el sensor
dht_sensor = adafruit_dht.DHT22(pin)

try:
    # Lee la temperatura y la humedad
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity

    print(f'Temperatura: {temperature:.2f}°C')
    print(f'Humedad: {humidity:.2f}%')

except RuntimeError as e:
    print(f'Error: {e}')
