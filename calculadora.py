import math
import time

def boas_vindas():
    """
    Exibe uma mensagem de boas-vindas e opções iniciais.
    """
    print("+-------------------------------+")
    print("|     BEM-VINDO(A) À CALCULADORA |")
    print("+-------------------------------+")
    print("|     1. Calculadora Científica  |")
    print("|     2. Calculadora Simples     |")
    print("+-------------------------------+")

def mostrar_menu_cientifica():
    """
    Exibe o menu da calculadora científica com opções de funções.
    """
    print('''
    ─────────────────────────────────
    |     Funções Disponíveis         |
    ─────────────────────────────────
    | 1. Calcular Seno                |
    | 2. Calcular Cosseno             |
    | 3. Calcular Tangente            |
    | 4. Voltar ao Menu Principal     |
    ─────────────────────────────────
    ''')

def mostrar_menu_calculadora_simples():
    """
    Exibe o menu da calculadora simples com opções de operações.
    """
    print('''
    ─────────────────────────────────
    |     Operações Disponíveis       |
    ─────────────────────────────────
    | 1. Adição                       |
    | 2. Subtração                    |
    | 3. Multiplicação                |
    | 4. Divisão                      |
    | 5. Voltar ao Menu Principal     |
    ─────────────────────────────────
    ''')

def calcular_seno(numero):
    print("Realizando a operação...")
    time.sleep(0.5)  # Pausa de 0.5 segundos
    return math.sin(numero)

def calcular_tangente(numero):
    print("Realizando a operação...")
    time.sleep(0.5)  # Pausa de 0.5 segundos
    return math.tan(numero)

def calcular_cosseno(numero):
    print("Realizando a operação...")
    time.sleep(0.5)  # Pausa de 0.5 segundos
    return math.cos(numero)

def calculadora_cientifica():
    """
    Gerencia as operações da calculadora científica.
    """
    while True:
        mostrar_menu_cientifica()
        try:
            escolha_funcao = int(input("Escolha a função para realizar a operação: "))
            if escolha_funcao == 4:
                break  # Finaliza e volta ao menu principal
            if escolha_funcao in [1, 2, 3]:
                try:
                    numero = float(input("Número: "))
                    if escolha_funcao == 1:
                        resultado = calcular_seno(numero)
                        print(f"Após realizar o cálculo de {numero}, o seno é: {resultado:.4f}")
                    elif escolha_funcao == 2:
                        resultado = calcular_cosseno(numero)
                        print(f"Após realizar o cálculo de {numero}, o cosseno é: {resultado:.4f}")
                    elif escolha_funcao == 3:
                        resultado = calcular_tangente(numero)
                        print(f"Após realizar o cálculo de {numero}, a tangente é: {resultado:.4f}")
                except ValueError:
                    print("Número inválido. Por favor, insira um número válido.")
            else:
                print("Operação inválida")
        except ValueError:
            print("Opção inválida. Por favor, insira um valor inteiro.")

def calculadora_simples():
    """
    Gerencia as operações da calculadora simples.
    """
    while True:
        mostrar_menu_calculadora_simples()
        try:
            escolha_funcao = int(input("Escolha a operação para realizar: "))
            if escolha_funcao == 5:
                break  # Volta ao menu principal
            if escolha_funcao in [1, 2, 3, 4]:
                try:
                    numero1 = float(input("Número 1: "))
                    numero2 = float(input("Número 2: "))
                    if escolha_funcao == 1:
                        resultado = numero1 + numero2
                        print("Realizando o cálculo...")
                        print(f"A soma: {numero1} + {numero2} = {resultado:.3f}")
                    elif escolha_funcao == 2:
                        resultado = numero1 - numero2
                        print("Realizando o cálculo...")
                        print(f"{numero1} - {numero2} = {resultado:.3f}")
                    elif escolha_funcao == 3:
                        resultado = numero1 * numero2
                        print("Realizando o cálculo...")
                        print(f"{numero1} * {numero2} = {resultado:.3f}")
                    elif escolha_funcao == 4:
                        if numero2 != 0:
                            resultado = numero1 / numero2
                            print("Realizando a divisão...")
                            print(f"A divisão: {numero1} / {numero2} = {resultado:.3f}")
                        else:
                            print("Erro: Divisão por zero não é permitida.")
                except ValueError:
                    print("Número inválido. Por favor, insira um número válido.")
            else:
                print("Operação não disponível")
        except ValueError:
            print("Opção inválida. Por favor, insira um valor inteiro.")

def escolher_opcao():
    """
    Permite ao usuário escolher entre calculadora científica ou simples.
    """
    while True:
        boas_vindas()
        try:
            opcao = int(input("Escolha a opção: "))
            if opcao == 1:
                calculadora_cientifica()
            elif opcao == 2:
                calculadora_simples()
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor inteiro.")

# Inicializa o programa
if __name__ == "__main__":
    escolher_opcao()
