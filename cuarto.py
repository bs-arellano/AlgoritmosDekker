'''
Garantiza exclusion mutua pero puede darse un bloqueo prolongado
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

        if thread_2:
            thread_1 = False

            time.sleep(0.001)
            thread_1 = True
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

        thread_2 = True

        if thread_1:
            thread_2 = False
            time.sleep(0.001)
            thread_2 = True
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