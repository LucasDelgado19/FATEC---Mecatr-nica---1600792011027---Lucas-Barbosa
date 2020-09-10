nomes = ['Delgado', 'Eduardo', 'Gomes', 'Henrique', 'Joao', 'Leonardo', 'Lira', 'Lucas', 'Matheus', 'Yago']


nomes.sort()

nome = input('Quem você deseja procurar?\n')

if nome in nomes:
  print ('Encontrei!', nome ,'está na lista!')
  print ('Encontrei na posição:', nomes.index(nome))
else:
  print ('Registro não encontrado...')
