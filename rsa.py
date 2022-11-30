import sys

deslocar = 2
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modInv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def gerarChave():
    p = int(input("Digite o p:\n"))
    q = int(input("Digite o q:\n"))
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = int(input("Digite o e:\n"))
            
    d = modInv(e, phi)
    
    print("Chave publica = [%d, %d]\n" % (e, n))
    print("Chave privada = [%d, %d]\n" % (d, n))
    
    return n, e, d
    
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def gerarE():
    p = int(input("Digite o p:\n"))
    q = int(input("Digite o q:\n"))
    
    phi = (p - 1) * (q - 1)
    
    e = 3
    while(mdc(e, phi) != 1):
        e += 2

    print("e =", e)
    
def encriptar(n, e):
    mensagem = input("Digite sua mensagem:\n")
    
    for palavra in mensagem:
        palavra = int(alfabeto.index(palavra) + deslocar)
        palavra = fastPowMod(palavra, e, n)
        print(palavra, end = ' ')
    print("\n")
    
def fastPowMod(base, exp, mod):
    if exp < 0:
        return 1 / fastPowMod(base, -exp, mod)
    ans = 1
    while exp:
        if exp & 1:
            ans = (ans * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return ans

def desencriptar(n, d):
    mensagem = input("Digite sua mensagem:\n")
    mensagem = mensagem.split()
    mensagem = [int(num) for num in mensagem]
    mensagem = [fastPowMod(num, d, n) for num in mensagem]
    mensagem = [alfabeto[num - deslocar] for num in mensagem]
    for letra in mensagem:
        print(letra, end = '')
    print("\n")
    
n = e = d = 0

if int(input("Escolha uma opcao:\n(0)-Gerar chaves\n(1)-Gerar (e)\n")):
    gerarE()
   
n, e, d = gerarChave()

while True:    
    if int(input("Digite:\n(0)-Encriptar\n(1)-Desencriptar\n")):
        desencriptar(n, d)

    else:
        encriptar(n, e)