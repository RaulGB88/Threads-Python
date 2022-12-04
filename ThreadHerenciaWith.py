import threading
import random

global variable_global
global lock

class miHilo(threading.Thread):
    def __init__(self):
        super(miHilo, self).__init__()
        self.operation = ''
        self.number = 0
    
    def run(self):
        global variable_global
        if self.operation == "div":
            numero = dividir(self.number)
            with lock:
                print(f"Soy el thread con nombre...: {self.name} Mi identificador es: ...: {self.operation} y el resultado del número dividido es...: {numero}\n", end="") 
                print(f'par: {self.number} dividido es: {numero},prueba {variable_global}\n', end='')
        else:
            self.operation = "multi"
            numero = multiplicar(self.number)
            with lock:
                variable_global = 'jaja'
                print(f"Soy el thread con nombre...: {self.name} Mi identificador es: ...: {self.operation} y el resultado del número multiplicado es...: {numero}\n", end="") 
                print(f'par: {self.number} multiplicado es: {numero}\n', end='')


def dividir(number):
    return number / 5


def multiplicar(number):
    return number * 5


def main():

    ListaHilos = []
    for i in range(10):
        if (i % 2) == 0:
            t = miHilo()
            t.operation = 'div'
            t.number = random.randint(0, 99)
            t.name = "dividir" + str(i)
        else:
            t = miHilo()
            t.operation = 'multi'
            t.number = random.randint(0, 99)
            t.name = "multiplicar" + str(i)
        
        ListaHilos.append(t)
        t.start()
        
if __name__ == "__main__":
    lock = threading.Lock()
    variable_global = 'VG1'
    main()
