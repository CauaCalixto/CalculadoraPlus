import math
import time

def boas_vindas():
    """
    Exibe uma mensagem de boas-vindas e opções iniciais.
    """
    print("+-------------------------------------------+")
    print("|     BEM-VINDO(A) À CALCULADORA            |")
    print("+-------------------------------------------+")
    print("|     1. Calculadora Científica             |")
    print("|     2. Calculadora Simples                |")
    print("|     3. Calculadora Formas Geometricas     |")
    print("|     4. Sair                               |")
    print("+-------------------------------------------+")

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
def mostrar_menu_formas_geometricas():
    '''Exibindo o menu de formas geometricas'''
    print('''
─────────────────────────────────
    |     Formas Disponiveis        |
    ─────────────────────────────────
    | 1. Triângulo                  |
    | 2. Círculo                    |
    | 3. Quadrado                   |
    | 4. Retângulo                  |
    | 5. Trapézio                   |
    | 6. Losango                    |
    | 7. Parelelogramo              |
    | 8. Héxagono regular           |
    | 9. Sair                       |
    ─────────────────────────────────''')
def calcular_triângulo(base, altura):
    area = base * altura / 2
    print("Realizando operação...")
    time.sleep(0.5)
    return area

def calcular_circulo(raio):
    area = math.pi * raio ** 2
    print("Realizando Operação...")
    time.sleep(0.5)
    return area

def calcular_quadrado(lado):
    area = lado * lado * 2
    print("Realizando operação...")
    time.sleep(0.5)
    return area

def calcular_retangulo(base, altura):
    area = base * altura
    print("Realizando operação")
    time.sleep(0.5)
    return area

def calcular_trapezio(base_maior, base_menor, altura):
    area = (base_maior + base_menor) * altura / 2
    print("Realizando Operação...")
    time.sleep(0.5)
    return area

def calcular_losango(diagonal_maior, diagonal_menor):
    area = diagonal_maior * diagonal_menor / 2
    print("Realizando operação...")
    time.sleep(0.5)
    return area

def calcular_paralelograma(base, altura):
    area = base * altura
    print("Realizando operação....")
    time.sleep(0.5)
    return area

def calcular_hexagono(lado):
    area = (3 * math.sqrt(3) * lado ** 2) / 2
    print("Realizando operação....")
    time.sleep(0.5)
    return area


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

def formas_geometricas():
    '''Gerenciando as formas geometricas'''
    while True:
        try:
            mostrar_menu_formas_geometricas()
            escolher_opcao = int(input("Selecione uma opção: "))
            if escolher_opcao == 9:
                break # Voltando ao menu 
            elif escolher_opcao == 1:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"Àrea do Triângulo é: {calcular_triângulo(base, altura)}")

            elif escolher_opcao == 2:
                raio = float(input("Raio: "))
                print(f"Àrea do circulo:{calcular_circulo(raio)}")

            elif escolher_opcao == 3:
                lado = int(input("Quantidade de lado: "))
                print(f"Perímetro: {calcular_quadrado(lado)}")

            elif escolher_opcao == 4:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"Àrea do Retângulo é: {calcular_retangulo(base, altura)}") 

            elif escolher_opcao == 5:
                base_maior = float(input("Base maior: "))
                base_menor = float(input("Base menor: "))
                altura = float(input("Altura: "))
                print(f"Àrea: {calcular_trapezio(base_maior, base_menor, altura)}")
            
            elif escolher_opcao == 6:
                diagonal_maior = float(input("Diagonal maior: "))
                diagonal_menor = float(input("Diagonal menor: "))
                print(f"Àrea: {calcular_losango(diagonal_maior, diagonal_menor)}")
            
            elif escolher_opcao == 7:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"Área: {calcular_paralelograma(base, altura)}")
            
            elif escolher_opcao == 8:
                lado = float(input("Lado: "))
                print(f"Área: {calcular_hexagono(lado)}")     
            else:
                    print("Opção inválida")

        except ValueError:
            print("Opção inválida")

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
            elif opcao == 3:
                formas_geometricas()
            elif opcao == 4:
                print("Até Logo...")
                break # Finalizando Programa
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor inteiro.")

# Inicializa o programa
if __name__ == "__main__":
    escolher_opcao()
