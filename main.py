#Tela inicial
print('''
Ola
      Bem vindo ao calc do anonimo feito em python
      so poderemos fazer contas de apenas 2 numeros (tanto int e float) e apenas soma e subtair
      irei adicionar mais coisas depois
      ''')

#Definir os valores da var dos numeros
n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))

#Explicar como que escolher entre soma e subtaçao
print('''voce poderar escolher entre soma e subtaçao sendo eles:

      soma: 1
      subtaçao: 2

      caso coloque um valor errado iriar da erro e o calc vai fecha''')

#Valor da var operaçao e tambem a parte das contas
operacao = int(input('operaçao: '))

if operacao == 1:
    print (n1, '+', n2, '=', n1 + n2)

elif operacao == 2:
    print (n1, '-', n2, '=', n1 - n2)

else:
    print ('''
    ERROR, voce colocou um valor que nao tava disponivel, porfavo inicie o programa novamente
    ''')

