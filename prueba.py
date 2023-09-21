import board
import digitalio
import busio 
print ( "¡Hola, flash!" ) # Intenta crear un 
pin de entrada digital = digitalio.DigitalInOut(board.D4) 
print ( "Digital IO ok!" ) # Intenta crear un dispositivo I2C 
i2c = busio .I2C(board.SCL, board.SDA) 
print ( "¡I2C ok!" ) # Intente crear un dispositivo SPI 
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO) 
print ( "SPI ok! " ) ( "¡hecho!" )