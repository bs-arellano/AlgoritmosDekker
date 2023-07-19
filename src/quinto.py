'''
Los procesos indican que quieren entrar en seccion critica, revisa si el segundo
quiere entrar. En caso afirmativo espera a que este cambie su bandera, en caso contrario
entra en seccion critica y luego cambia su bandera
'''
import threading
import time

def Proceso1(id):

    global thread_1
    global thread_2
    global turno

    completado = False

    print(f"Proceso {id} listo")

    while not completado:

        thread_1 = True

        if thread_2:
            if turno!=1:
                thread_1 = False
                while(turno!=1):
                    pass
                thread_1 = True
        else:
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            thread_1=False
            turno=2

def Proceso2(id):
    global thread_1
    global thread_2
    global turno
    completado = False

    print(f"Proceso {id} listo")

    while not completado:

        thread_2 = True

        if thread_1:
            if turno!=2:
                thread_2 = False
                while turno!=2:
                    pass
                thread_2 = True
        else:
            print(f"Ejecutando proceso {id}")
            time.sleep(2)
            print(f"Proceso {id} finalizado")
            completado=True
            thread_2=False
            turno=1

hilo_1 = threading.Thread(target=Proceso1, args=(1,))
hilo_2 = threading.Thread(target=Proceso2,args=(2,))
thread_1=False
thread_2=False
turno=2
hilo_1.start()
hilo_2.start()