import board
import adafruit_dht

# Configura el pin GPIO al que está conectado el sensor
pin = board.D4  # Reemplaza con el número de pin correcto

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
