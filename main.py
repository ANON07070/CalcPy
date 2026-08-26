import argparse


# defs do argparse
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
    confimacao_divicao(n1, n2)
    conta(n1, n2)


# def do codigo CLI
def var():     #Definir os valores da var dos numeros
    while True:
        try:
            n1 = float(input('Primeiro numero: ')) #var do primeiro numero
            print(f'Voce escolher {n1} como primeiro numero')
            break
        except ValueError:
            print('Por favor, insira um número válido.')
    while True:
        try:
            n2 = float(input('Segundo numero: ')) #var do segundo numero
            print(f'Voce escolheu {n2} como segundo numero')
            break
        except ValueError:
            print('Por favor, insira um número válido.')
    return n1, n2


def home():     #Definir a home do programa
    print('''\n
Bem-vindo ao calc do anon feito em python
        \n''')

def confimacao_divicao(n1, n2):     #Definir a confimaçao do programa
    if n2 == 0:
        print('''
Como voce colocou 0 como segundo numero, nao da para dividir por 0
        ''')
        confimacao = input(str('Voce quer continuar? (S/N): '))
        if confimacao == 'S':
            print ('''
Ok''')
            return
        else:
            print ('''
Entendo, por favor inicie o programa novamente e coloque um valor correto
            ''')
        exit()

def conta(n1, n2):      #Definir a conta do programa
    #Explicar como que escolher entre soma e subtaçao
    print('''
Voce precisa escolher entre as seguintes operaçoes:

        soma: 1
        subtaçao: 2
        multiplicaçao: 3
        divisao: 4

caso coloque um valor errado iriar da erro
        ''')


    while True:
        try:
            operacao = int(input('operação: '))
            if operacao not in [1, 2, 3, 4]:
                print('Por favor, insira um número válido entre 1 e 4.')
                continue
            break
        except ValueError:
            print('Por favor, insira um número válido.')

    operacao_dicionario ={
        1: ('+', n1 + n2),
        2: ('-', n1 - n2),
        3: ('*', n1 * n2),
        4: ('/', n1 / n2 if n2 != 0 else None)
    }

    resultado = operacao_dicionario.get(operacao)
    if resultado and resultado[1] is not None:
        print(f'{n1} {resultado[0]} {n2} = {resultado[1]}')
    elif operacao == 4 and n2 == 0:
        print('Erro: não é possível dividir por 0')
    nova_conta()

def nova_conta():
    while True:
        nova_conta = input(str('Voce quer fazer uma nova conta? (S/N): '))
        if nova_conta == 'S' or 's':
            print ('''
Ok, vamos fazer uma nova conta
            ''')
            n1, n2 = var()
            confimacao_divicao(n1, n2)
            conta(n1, n2)
            break
        else:
            print ('''Ok, entendo, por favor inicie o programa novamente caso queira fazer uma nova conta''')
            exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nPrograma interrompido.')
        exit()