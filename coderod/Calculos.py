import random
import math
import os
import random
def MDC(a, b):

    if(a % b == 0):
        return b
    else:
        return MDC(b, a % b)
def linear(a, b, array, b2):

    q = a // b

    if(a % b == 0):

        i = len(array) - 1
        valor = 0
        multiplicador = 1
        anterior = 0
        resul = list()
        print(array)
        while (i > 0):
            print(array[i])

            valor = array[i] * multiplicador + anterior
            anterior = multiplicador
            multiplicador = valor
            resul.append(valor)

            i = i - 1
        s = resul[len(resul) - 1]
        print(resul)
        if (len(resul) - 1) % 2 == 0:
            s = s * -1
        while s < 1:
            s = s + b2
        print(s)
        return s
    else:
        array.append(q)
        return linear(b, a % b, array, b2)

def limpar_terminal():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def exponenciacao_modular_rapida(m, e, n):
    if (e == 0):
        return 1
    elif (e % 2 == 0):
        aux = exponenciacao_modular_rapida(m, e / 2, n)
        return (aux ** 2) % n
    else:
        return (m % n * exponenciacao_modular_rapida(m, e - 1, n)) % n

def codificar(char, e, n):

    alfabeto = {'A':2, 'B': 3, 'C':4, 'D':5, 'E': 6, 'F': 7,
    'G' : 8, 'H': 9, 'I' : 10, 'J' : 11 , 'K' : 12, 'L': 13,
    'M': 14, 'N': 15, 'O' : 16, 'P' : 17, 'Q' : 18, 'R': 19, 'S': 20,
    'T': 21, 'U': 22, 'V' : 23, 'W': 24, 'X': 25, 'Y': 26, 'Z':27, ' ': 28}

    arquivo = open('mensagem_encriptada.txt', 'w')

    for i in char:
        caracter_encriptado = exponenciacao_modular_rapida(alfabeto[i], e, n)
        arquivo.write('{} '.format(caracter_encriptado))

    arquivo.close()

def descriptografar(msg, d, n):

    alfabeto_inverso = {2 : 'A', 3: 'B', 4: 'C', 5 : 'D', 6 :'E', 7: 'F',
                8: 'G', 9: 'H', 10 : 'I', 11 : 'J', 12: 'K', 13:'L',
                14:'M', 15:'N', 16: 'O', 17: 'P', 18: 'Q', 19: 'R', 20: 'S',
                21: 'T', 22 : 'U', 23: 'V', 24: 'W', 25 : 'X', 26 : 'Y', 27: 'Z', 28:' '}


    mensagem = list()

    file = open('mensagem_desncriptada.txt', 'w')
    for number in msg:
        number.rstrip()
        number = number.split()
        mensagem.extend(number)

    for i in mensagem:
        i = int(i)
        y = exponenciacao_modular_rapida(i, d, n)
        file.write('{}'.format(alfabeto_inverso[y]))

    file.close()

def primalidade(number):

    if number <= 1:
        return False
    else:
        aux = math.ceil(math.sqrt(number))

        for i in range(2, aux + 1):
            if number % i == 0:
                return False
        return True

def primos_entre_si(e, phi):
    if MDC(e, phi) == 1:
        return True
    else:
        return False