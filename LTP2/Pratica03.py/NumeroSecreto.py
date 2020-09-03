numero_secreto = 18
palpite = int(input('Informe um número entre 0 e 100:'))
if palpite == numero_secreto:
  print('Acertou!')
else:
  if palpite > numero_secreto:
    print('Errou! Mais pra baixo!')
  else:
    print ('Errou! Mais pra cima!') 
