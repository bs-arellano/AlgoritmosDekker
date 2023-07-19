'''
Problema: Si un proceso falla en seccion critica el otro queda bloqueado esperando la señal
Ademas no se garantiza exclusion mutua:
- P1 encuentra thread_2=falso
- P2 encuentra thread_1=falso
- P1 pone thread_1=true y entra en seccion critica
- P2 pone thread_2=true y entra en seccion critica
'''

import threading
import time

def Proceso1(id):
    print(f"Proceso {id} listo")
    global thread_1
    global thread_2
    completado = False
    while not completado:
        if thread_2:
            pass
        else:
            thread_1 = True
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            thread_1=False

def Proceso2(id):
    print(f"Proceso {id} listo")
    global thread_1
    global thread_2
    completado = False
    while not completado:
        if thread_1:
            pass
        else:
            thread_2 = True
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            thread_2=False

hilo_1 = threading.Thread(target=Proceso1, args=(1,))
hilo_2 = threading.Thread(target=Proceso2,args=(2,))
thread_1=False
thread_2=False
hilo_1.start()
hilo_2.start()