#Tela inicial
print('''
      Ola!
      Bem vindo ao calc do anonimo feito em python
      so poderemos fazer contas de apenas 2 numeros (tanto int e float) e tenhos soma, subtair, multiplicaçao e divisao
      irei adicionar mais coisas depois
      ''')

#Definir os valores da var dos numeros
n1 = float(input('Primeiro numero: '))
print(f'voce escolher {n1} como primeiro numero')
n2 = float(input('Segundo numero: '))
print(f'voce escolheu {n2} como segundo numero')

#confimaçao se o n2 nao e 0
if n2 == 0:
    print('''
    como voce escolheu 0 no segundo numero, isso esta certo?
    ''')
    confimacao = input('voce quer continuar? (S/N): ')
    if confimacao == 'S':
         print ('''
    Ok''')
    else:
        print ('''
        entendido, se voce quiser escolher outro numero porfavo inicie novamente o programa
        ''')
    exit()


#Explicar como que escolher entre soma e subtaçao
print('''
      voce poderar escolher entre essas 4 opçoes sendo eles:

      soma: 1
      subtaçao: 2
      multiplicaçao: 3
      divisao: 4

      caso coloque um valor errado iriar da erro e o calc vai fecha
      ''')

#Valor da var operaçao e tambem a parte das contas
operacao = int(input('operaçao: '))


if operacao == 1: #soma
    print (n1, '+', n2, '=', n1 + n2)

elif operacao == 2: #subtaçao
    print (n1, '-', n2, '=', n1 - n2)

elif operacao == 3: #multiplicaçao
    print (n1, 'x', n2, '=', n1 * n2)

elif operacao == 4: #divisao
    if n2 == 0:
        print('nao da para dividi por 0, se voce quiser escolher outro numeros por favo inicie o programa novamente')
        exit()
    print (n1, '/', n2, '=', n1 / n2)


else: #valor errado
    print ('''
    ! ERROR !, voce colocou um valor que nao tava disponivel, porfavo inicie o programa novamente
    ''')

