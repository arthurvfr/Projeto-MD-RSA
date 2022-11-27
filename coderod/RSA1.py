import Calculos
import chavepublica as cp
import interface

while (True):

    interface.main()
    opcao = input("----------| DIGITE SUA OPCAO: ")

    if opcao == '1':

        cp.chave_publica()

        Calculos.limpar_terminal()
        continue

    if opcao == '2':

        interface.cp()


        public_key = input("DIGITE O NOME DO ARQUIVO(SEM A EXTENSÃO): ")
        public_key = public_key + '.txt'
        chave = open(public_key)


        lst = list()

        for line in chave:
            line = line.rstrip()
            numbers = line.split()
            lst.extend(numbers)

        n = int(lst[0])
        e = int(lst[1])

        interface.arquvo_mensagem()
        escolha = input('--> ')
        
        if escolha == '1':
            ih = input('DIGITE O NOME DO ARQUIVO(SEM EXTENSÃO):-> ')
            ih = ih + '.txt'
            string = open(ih)

            msgn = ''
            for line in string:
                msgn += line
            print(msgn)
            
        else:
            print('DIGITE UMA MENSAGEM:\n')
            msgn = input('--> ')

        msgn.upper()

        Calculos.codificar(msgn, e, n)

        Calculos.limpar_terminal()

        continue

    if opcao == '3':


        interface.p_and_q()

        escolha = int(input('-> '))

        if escolha == 1:

            fop = input('DIGITE O NOME DO ARQUVO(SEM EXTENSÕES): --> ')
            fop = fop + '.txt'
            fh1 = open(fop)

            lista = list()

            for line in fh1:
                line.rstrip()
                line = line.split()
                lista.extend(line)
            p = lista[0]
            q = lista[1]
            e = lista[2]

            print('\n')

        else:
            p = int(input('Digite (p): '))
            q = int(input('digite (q): '))
            e = int(input('Digite (e): '))

        phi = (int(p) - 1) * (int(q) - 1)
        e = int(e)
        n = int(p) * int(q)

        fh = input('DIGITE O NOME DO ARQUIVO(SEM A EXTENSÃO) A SER DESCRIPTADO: --> ')

        fh = fh + '.txt'
        arquivo = open(fh)

        b = phi
        array = list()
        d = Calculos.linear(e, phi, array, b)

        Calculos.descriptografar(arquivo, d, n)

        Calculos.limpar_terminal()
        continue

    if int(opcao) > 3 or int(opcao) < 1:
        break