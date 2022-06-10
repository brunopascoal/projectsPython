from time import sleep

print('BEM-VINDO AO CAIXA ELETRONICO')
numero = int(input('Valor para sacar: '))

cem = int(numero / 100)
numero = numero % 100
  
cinquenta = int(numero/50)
numero = numero % 50

vinte = int(numero/20)
numero = numero % 20

dez = int(numero/10)
numero = numero % 10

um = numero
  
if cem > 0:
  print('Processando o saque...')
  sleep(2)
  print(f'{cem} nota(s) R$100,00 ')
if cinquenta > 0:
  print('Processando o saque...')
  sleep(2)
  print(f'{cinquenta} nota(s) R$ 50,00')
if vinte > 0:
  print('Processando o saque...')
  sleep(2)
  print(f'{vinte} nota(s) R$ 20,00')
if dez > 0:
  print('Processando o saque...')
  sleep(2)
  print(f'{dez} nota(s) R$  10,00')
   
if numero > 0:
  print(f'Saldo restante: R${numero},00. Não pode ser sacado devido a falta de cédulas menores que R$ 10,00')