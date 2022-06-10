from random import randint
from time import sleep

print('=*='*10)
print('      JOGO NA MEGA SENA')
print('=*='*10)
lista = []
lista_jogo = []
n=int(input('Quanto jogos você quer jogar?: '))
for d in range(0, 6):
    numero = int(input('Digite os valores para qualquer jogo: '))
    lista_jogo.append(numero)
    lista_jogo.sort()
print(lista_jogo)
for c in range(0, n):
    lista.append([])
print()
for c in range(0, n):
    for d in range(0, 6):
        lista[c].append(randint(0, 100000))
sleep(1)
print(f'=-=-=-=- SORTEANDO {n} JOGOS =-=-=-=-')
sleep(1)
for c in range(0, n):
    lista[c].sort()
    print(f'Jogo {c+1}: {lista[c]}', end=' ')
    print()
    sleep(1)
for e in range(0, n):
    if lista_jogo == lista[e]:
        resultado = f'VOCÊ GANHOU O jogo {e+1}!'
    else:
        resultado = 'VOCE NÂO GANHOU'
print()
print(f'=-=-=-=-      {resultado}     =-=-=-=-')

