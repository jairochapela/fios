from threading import Thread
from time import sleep

class Contador(Thread):
    def __init__(self, nombre):
        super().__init__(name=nombre)

    def run(self):
        for i in range(10):
            print(self.name, i)
            sleep(0.5)
    

t1 = Contador("María")
t2 = Contador("José")

t1.start()
t2.start()