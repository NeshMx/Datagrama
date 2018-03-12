# Instituto Tecnológico de Querétaro    Administración de Redes

'''
datagrama.py - Genera datagramas a partir de un mensaje cifrado
utilizando la librería string_to_binary y escribe un log con los
datagramas
'''

# Status|IP|MENSAJE BINARIO|ACK

import socket
from random import randrange
import string_to_binary
import sys

count = 0

def getStatus():
    return randrange(3)

def getDatagram():
    status = getStatus()
    ip = str(socket.gethostbyname(socket.gethostname()))
    msgBin = "".join(string_to_binary.b)
    return "{}|{}|{}|Fin\n".format(status, ip, msgBin)

def menu():
    print("-" * 30 + "MENU" + "-" * 30)
    print("1. Mostrar el datagrama")
    print("2. Generar log_file")
    print("0. Salir")
    print("-" * 67)
    choice = int(input("Elija la opción deseada [0-2]: "))
    if choice == 1:
        print("\n" + "Datagrama " + str(count) + ": ")
        print(getDatagram())
    elif choice == 2:
        writeLog()
    elif choice == 0:
        print("¡Baygon!")
        sys.exit()
    else:
        int(input("Opción no válida. Presione cualquier tecla para intentarlo de nuevo..."))

def writeLog():
    fh = open("log.ahc", "a")
    lines = [getDatagram()]
    fh.writelines(lines)
    fh.close

while True:
    menu()    
    count += 1

# Huerta Campos Alejandro
