import threading
import random

global variable_global
global lock

def funcionMiHilo(operation, number):
    global variable_global
    if operation == "div":
        numero = dividir(number)
        lock.acquire()
        print(f"Soy el thread con nombre...: {threading.Thread.name} Mi identificador es: ...: {operation} y el resultado del número dividido es...: {numero}\n", end="") 
        print(f'par: {number} dividido es: {numero},prueba {variable_global}\n', end='')
        lock.release()
    else:
        operation = "multi"
        numero = multiplicar(number)
        lock.acquire()
        variable_global = 'jaja'
        print(f"Soy el thread con nombre...: {threading.Thread.name} Mi identificador es: ...: {operation} y el resultado del número multiplicado es...: {numero}\n", end="") 
        print(f'par: {number} multiplicado es: {numero}\n', end='')
        lock.release()


def dividir(number):
    return number / 5


def multiplicar(number):
    return number * 5


def main():

    ListaHilos = []
    for i in range(10):
        if (i % 2) == 0:
            operation = 'div'
            number = random.randint(0, 99)
            t = threading.Thread(target=funcionMiHilo, args=(operation, number))
            t.name = "dividir" + str(i)
        else:
            operation = 'multi'
            number = random.randint(0, 99)
            t = threading.Thread(target=funcionMiHilo, args=(operation, number))
            t.name = "multiplicar" + str(i)
        
        ListaHilos.append(t)
        t.start()
        
if __name__ == "__main__":
    lock = threading.Lock()
    variable_global = 'VG1'
    main()
