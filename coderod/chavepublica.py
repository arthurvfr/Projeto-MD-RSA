import Calculos
import os
import sys
import interface
def chave_publica():

    while(True):
        p = int(input('Digite (p): '))
        q = int(input('Digite (q): '))
        if p == q:
            interface.error_iguais()
            continue
        if p * q < 28:
            interface.error_menor_28()
            continue
        if (Calculos.primalidade(p) == False or Calculos.primalidade(q) == False):
            interface.error_primos()
            continue
        else:
            break
    phi = (p - 1) * (q - 1)
    n = p * q

    e = int(input('Digite um (e): '))
    while True:
        if e <= 1:
            interface.erros_e()
            e = int(input("Digite um (e): "))
            continue

        if e >= phi:
            interface.erros_e()
            e = int(input("Digite um (e): "))

            continue
        else:
            if Calculos.primos_entre_si(e, n) == True:
                break
            else:
                interface.erros_e()
                e = int(input("Digite um (e): "))
                continue
    arquivo = open('chave_publica.txt', 'w')
    arquivo.write('{} {}'.format(n, e))
    arquivo.close()

    fh = open('p_and_q.txt', 'w')
    fh.write('{} {} {}'.format(p, q, e))
    fh.close()
