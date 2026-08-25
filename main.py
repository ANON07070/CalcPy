import argparse
def info():
    parser = argparse.ArgumentParser(description='''\n
    Calculadora simples

    de inicio voce precisa colocar dois numeros, e depois escolher entre soma, subtraçao, multiplicaçao e divisao
    a escolha funciona assim, voce coloca o primeiro numero e em seguinda ira coloca o segundo numero, apois isso ira aparece uma opçao de 1 a 4 sendo eles
    1 = soma
    2 = subtaçao
    3 = multiplicaçao
    4 = diviçao
    \n''')    
    parser.add_argument('--version', action='version', version='1.0')
    parser.add_argument('n1', type=float, help='Primeiro numero')
    parser.add_argument('n2', type=float, help='Segundo numero')
    parser.add_argument('-O', '--operacao', type=int, choices=[1, 2, 3, 4],
    
                        required=True, help='1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão')
    args = parser.parse_args()
    return args

def conta_argparse(n1, n2, operacao):
    if operacao == 4 and n2 == 0:
        print('Erro: não é possível dividir por 0')
        return
    operacoes = {
        1: ('+', n1 + n2),
        2: ('-', n1 - n2),
        3: ('x', n1 * n2),
        4: ('/', n1 / n2 if n2 != 0 else None)
    }
    simbolo, resultado = operacoes[operacao]
    print(f'{n1} {simbolo} {n2} = {resultado}')

# definindo def #

#def main

def main():
    # Se houver argumentos no terminal,
    # usa o argparse.
    import sys

    if len(sys.argv) > 1:
        args = info()
        conta_argparse(args.n1, args.n2, args.operacao)
        return

    # Se não houver argumentos,
    # usa o modo normal.
    home()
    n1, n2 = var()
    confimacao(n1, n2)
    conta(n1, n2)

    
def var():
    # Definir os valores da var dos numeros #
    n1 = float(input('Primeiro numero: ')) #var do primeiro numero
    print(f'voce escolher {n1} como primeiro numero')
    n2 = float(input('Segundo numero: ')) #var do segundo numero
    print(f'voce escolheu {n2} como segundo numero')
    return n1, n2

#def da Home
def home():
    print('''\n
        Bem-vindo ao calc do anon feito em python
        \n''')

#def da confimaçao se o n2 nao e 0
def confimacao(n1, n2):
    if n2 == 0:
        print('''
        como voce escolheu 0 no segundo numero, isso esta certo?
        ''')
        confimacao = input(str('voce quer continuar? (S/N): '))
        if confimacao == 'S':
            print ('''
        Ok''')
            return
        else:
            print ('''
            entendido, se voce quiser escolher outro numero porfavo inicie novamente o programa
            ''')
        exit()

#def da conta
def conta(n1, n2):
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




##############################
# Chamando def e defindo var #
##############################

if __name__ == "__main__":
    main()