# SPDX-FileCopyrightText: 2021 ladyada para Adafruit Industries 
# SPDX-License-Identifier: MIT

importar tiempo
importar tablero
importar adafruit_dht

# Inicialice el dispositivo dht, con el pin de datos conectado a:
dhtDevice = adafruit_dht.DHT22(board.D4)

# puedes pasar DHT22 use_pulseio=False si no quieres usar pulseio. 
# Esto puede ser necesario en una computadora de placa única con Linux como Raspberry Pi, 
# pero no funcionará en CircuitPython. 
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

mientras que  Verdadero :
     intente :
         # Imprima los valores en el puerto serie
        temperatura_c = dhtDevice.temperatura
        temperatura_f = temperatura_c * ( 9 / 5 ) + 32
        humedad = dhtDevice.humedad
        print (
             "Temp: {:.1f} F / {:.1f} C Humedad: {}% " . formato (
                temperatura_f, temperatura_c, humedad
            )
        )

    excepto RuntimeError como error:
         # Los errores ocurren con bastante frecuencia, los DHT son difíciles de leer, simplemente continúe 
        imprimiendo (error.args[ 0 ])
        time.sleep( 2.0 )
         continúa 
    excepto Excepción como error:
        dhtDevice.salir()
        generar error

    tiempo.dormir( 2.0 )