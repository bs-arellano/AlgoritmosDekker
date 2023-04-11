import threading
import time

def Proceso1(id):
    global thread_1
    global thread_2
    global turno
    while True:
        thread_1=True
        turno=2
        time.sleep(0.5)
        while thread_2 and turno==2:
            pass
        print(f"Ejecutando proceso {id}")
        time.sleep(2)
        print(f"Proceso {id} finalizado")
        thread_1=False
        break

def Proceso2(id):
    global thread_1
    global thread_2
    global turno
    while True:
        thread_2=True
        turno=1
        time.sleep(0.5)
        while thread_1 and turno==1:
            pass
        print(f"Ejecutando proceso {id}")
        time.sleep(2)
        print(f"Proceso {id} finalizado")
        thread_2=False
        break

a = threading.Thread(target=Proceso1,args=(1,))
b = threading.Thread(target=Proceso2,args=(2,))
turno
thread_1=False
thread_2=False
a.start()
b.start()