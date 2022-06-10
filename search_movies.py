import requests
import json

req = None

while True:
   try:
      nome_filme = input('Digite o nome do Filme ou sair: ')
      if nome_filme == 'sair':
          break
      req = requests.get('http://www.omdbapi.com/?apikey=5d9cabe3&t=' + nome_filme)
      dict = json.loads(req.text)
      print('\033[31mTitulo:\033[0;0m', dict['Title'])
      print('\033[31mAno:\033[0;0m', dict['Year'])
      print('\033[31mEscritor(es):\033[0;0m', dict['Writer'])
      print('\033[31mAtores:\033[0;0m', dict['Actors'])
      print('\033[31mNota:\033[0;0m', dict['imdbRating'])
      print()
      print()
   except:
      print('Erro no request. Ou limite de request diario atingido.')
      exit()