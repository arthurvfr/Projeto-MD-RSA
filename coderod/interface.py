def main():
    print('****************************************************************************************')
    print('--------------------------PROJETO RSA---------------------------------------------------')
    print('****************************************************************************************')
    print('-------------------------<ESCOLHA UMA DAS OPÇÕES ABAIXO>---------------------------------')
    print('\n')
    print('-----------------------| 1 - CHAVE PUBLICA |----------------------------------------------')
    print('-----------------------| 2 - ENCRIPTAR |--------------------------------------------------')
    print('-----------------------| 3 - DESENCRIPTAR |-----------------------------------------------')
    print('-----------------------| 4 - SAIR |-------------------------------------------------------')
    print('\n')
    print('\n')

def error_primos():

    print('------| P OU Q NÃO ERA PRIMO POR FAVOR DIGITE-OS NOVAMENTE |-------------------------------')

def error_menor_28():
    print('------| p * q < 28, POR FAVOR DIGITE-OS NOVAMENTE |-----------------------------------------')

def error_iguais():
    print('------| p e q SÃO IGUAIS,POR FAVOR DIGITE-OS NOVAMENTE | ------------------------------------')
def erros_e():
        print('-----| (e) É UM VALOR QUE NÃO ATENDE OS REQUISITOS, POR FAVOR DIGITE NOVAMENTE | -----------')

def p_and_q():
    print('---------| DESEJA USAR UM ARQUIVO COM p,q,e ?|--------------')
    print('----------| SIM:(1) NÃO:(0) |----------------------------------')
def cp():
    print('---------| DIGITE UM ARQUIVO EXTERNO DE CHAVE PÚBLICA |--------------\n\n')
def arquvo_mensagem():
    print('---------| DESEJA USAR UM ARQUVIO DE MENSAGEM JA PREDIFINIDO? |-----------\n')
    print('---------| SIM : (1) NÃO : (0) |------------------------------')