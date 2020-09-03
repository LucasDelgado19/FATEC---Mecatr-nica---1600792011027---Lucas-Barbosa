from os import system 
from math import sin, cos, radians
import math

def mostrar_menu():
  system('clear')
  print('0 -> Sair')
  print('+ -> Somar')
  print('- -> Subtrair')
  print('* -> Multiplicar')
  print('/ -> Dividir')
  print('sen -> Seno')
  print('cos -> Cosseno')
  print('elevado -> Potência')
  print('raiz -> Calcular raiz')

def somar():
  numero1 = float(input('Numero 1:'))
  numero2 = float(input('Numero 2:'))
  resultado = numero1 + numero2
  print ('Resultado da soma:', resultado)

def subtrair():
  numero1 = float(input('Numero 1:'))
  numero2 = float(input('Numero 2:'))
  resultado = numero1 - numero2
  print ('Resultado da subtração:', resultado)

def multiplicar():
  numero1 = float(input('Numero 1:'))
  numero2 = float(input('Numero 2:'))
  resultado = numero1 * numero2
  print ('Resultado da subtração:', resultado)

def dividir():
  numero1 = float(input('Numero 1:'))
  numero2 = float(input('Numero 2:'))
  resultado = numero1 / numero2
  print ('Resultado da subtração:', resultado)

def seno():
  angulo=float(input("Angulo:"))
  print('Seno do ângulo é:', sin(radians(angulo)))

def cosseno():
  angulo=float(input("Angulo:"))
  print('Seno do ângulo é:', cos(radians(angulo)))

def potencia():
  numero1 = float(input('A base:'))
  numero2 = float(input('Elevado a:'))
  resultado = numero1 ** numero2
  print ('O', numero1,'elevado a', numero2,'é igual a:', resultado)

def raiz():
  numero = float(input('Coloque o valor da raiz:'))
  resultado = math.sqrt(numero)
  print ('A raiz de', numero, 'é:', resultado)

ligado = True

while ligado == True:
  mostrar_menu()
  opcao = input ('Opcao:')
  if opcao == '0':
    ligado = False
  elif opcao == '+':
    somar()
  elif opcao == '-':
    subtrair()
  elif opcao == '*':
    multiplicar()
  elif opcao == '/':
    dividir()
  elif opcao == 'sen':
    seno()
  elif opcao == 'cos':
    cosseno()
  elif opcao == 'elevado':
    potencia()
  elif opcao == 'raiz':
    raiz()

  input ('Pressione ENTER para continuar...')
    
print ('Até logo!')
