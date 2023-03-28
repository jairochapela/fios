from threading import Thread

def contar():
    for i in range(10):
        print(i)

# Construcción de dos hilos: t1 y t2
t1 = Thread(target=contar)
t2 = Thread(target=contar)

# Puesta en marcha de los dos hilos
t1.start()
t2.start()

