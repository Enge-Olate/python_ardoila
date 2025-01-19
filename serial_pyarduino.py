
import serial
import time

receptor = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    timeout=1
)

time.sleep(2)

def enviar_dado(dado):
    receptor.write(dado.encode())
    time.sleep(1)

enviar_dado('1')
time.sleep(2)
enviar_dado('0')
receptor.close()

    