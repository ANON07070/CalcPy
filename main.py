n1 = float(input('n1: '))
n2 = float(input('n2: '))

print('''escolha qual operaçao voce vai usar
soma = 1
subtaçao = 2''')
operacao = int(input('operaçao: '))

if operacao == 1:
    print (n1, '+', n2, '=', n1 + n2)

elif operacao == 2:
    print (n1, '-', n2, '=', n1 - n2)

else:
    print ('erro')

