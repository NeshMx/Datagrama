# Instituto Tecnológico de Querétaro    Administración de Redes

# string_to_binary.py - librería para cifrar a binario un mensaje y descifrar a texto.

import binascii

def toBin(s):    
    b = [bin(ord(x))[2:].zfill(8) for x in s]
    # msgBin = "|".join(b)
    # print("--CIFRADO BINARIO--")
    # print(msgBin)
    return b

def toString(b):
    print("--DESCIFRADO BINARIO--")
    return "".join([chr(int(x,2)) for x in b])
    
s = input("Palabra a cifrar: ")
b = toBin(s)
# s2 = toString(b)
# print("Mensaje: " + s2)

# Huerta Campos Alejandro