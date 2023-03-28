from threading import Thread

class Acumulador(Thread):
    numero = 0

    def run(self):
        for i in range(1000000):
            a = Acumulador.numero
            a += 1
            Acumulador.numero = a


t1 = Acumulador()
t2 = Acumulador()

print("Antes", Acumulador.numero)
t1.start()
t2.start()
t1.join()
t2.join()
print("Después", Acumulador.numero)