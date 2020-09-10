nomes = []

continuar = True

while continuar == True:
  nome = input('Informe um nome:')
  nomes.append (nome)
  print (nomes)
  if input ('Deseja continuar S ou N? \n') == 'S':
    continuar = True
  else:
    continuar = False 
print ('\n')    
nomes.sort()
print ('Os nomes em ordem alfabetica:')
print (nomes)
