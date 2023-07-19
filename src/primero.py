'''
Problema: Los procesos largos castigan a los procesos cortos
'''

import threading
import time

def Proceso1(id):
    print(f"Proceso {id} listo")
    global turno
    completado = False
    while not completado:
        if turno!=1:
            pass
        else:
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            #time.sleep(10)
            print(f"Proceso {id} finalizado")
            completado=True
            turno=2

def Proceso2(id):
    print(f"Proceso {id} listo")
    global turno
    completado = False
    while not completado:
        if turno!=2:
            pass
        else:
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            turno=1

turno = 1
hilo_1 = threading.Thread(target=Proceso1, args=(1,))
hilo_2 = threading.Thread(target=Proceso2, args=(2,))
hilo_1.start()
hilo_2.start()