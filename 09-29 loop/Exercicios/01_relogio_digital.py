# Crie um programa que conte de 0 até 59 segundos, simulando um relógio.

import time

segundos = 0
while segundos < 60:
    print(f'{segundos:02d} segundos')
    time.sleep(1)
    segundos += 1
print('Um minuto se passou')
