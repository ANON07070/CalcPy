# CalcPy

Calculadora simples de terminal feita em Python.

O CalcPy foi meu primeiro projeto em Python e foi desenvolvido para praticar conceitos básicos da linguagem, como funções, tratamento de erros, dicionários, entrada de dados e argumentos de linha de comando.

## 🖥️ Uso

Ao iniciar o programa normalmente, você pode informar dois números e escolher uma das quatro operações:

* `1` — Soma
* `2` — Subtração
* `3` — Multiplicação
* `4` — Divisão

O programa também verifica entradas inválidas e impede a divisão por zero.

### Linha de comando

O CalcPy também pode ser utilizado passando os números e a operação diretamente pelo terminal através do `argparse`.

Exemplo:

```bash
python main.py 10 5 --operacao 1
```

Resultado:

```text
10.0 + 5.0 = 15.0
```

Para ver a versão:

```bash
python main.py --version
```

## ✨ Funcionalidades

* Soma, subtração, multiplicação e divisão
* Entrada de números decimais
* Validação de entradas
* Proteção contra divisão por zero
* Possibilidade de realizar várias contas na mesma execução
* Uso interativo pelo terminal
* Suporte a argumentos de linha de comando com `argparse`
* Interrupção do programa com `Ctrl+C` tratada de forma amigável

## 📚 Objetivo

Este projeto foi criado como uma forma de colocar em prática os conhecimentos adquiridos durante meus primeiros estudos em Python.

Foi também meu primeiro projeto completo desenvolvido em Python.

## 🤖 Uso de Inteligência Artificial

A inteligência artificial **não foi utilizada para escrever ou gerar o código deste projeto**.

Ela foi utilizada apenas como ferramenta de apoio durante o desenvolvimento, principalmente para ajudar a entender e solucionar problemas encontrados ao longo do projeto.
