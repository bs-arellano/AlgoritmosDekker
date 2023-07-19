'''
Se garantiza exlusion mutua
Problema: Si ambos procesos marcan su bandera al tiempo se genera interbloqueo
'''
import threading
import time

def Proceso1(id):

    global thread_1
    global thread_2
    completado = False

    print(f"Proceso {id} listo")

    while not completado:

        thread_1 = True
        time.sleep(0.1)

        if thread_2:
            pass
        else:
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            thread_1=False

def Proceso2(id):
    global thread_1
    global thread_2
    completado = False

    print(f"Proceso {id} listo")

    while not completado:

        #time.sleep(0.2)
        thread_2 = True
        time.sleep(0.1)

        if thread_1:
            pass
        else:
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