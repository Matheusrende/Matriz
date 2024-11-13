import numpy as np
from fractions import Fraction

# Função principal que executa o programa
def main():
    while True:
        
        escolha = getopcao()
        
        # Executa a função correspondente com base na escolha do usuário
        if escolha == 1:
            calculo_de_matriz()
        elif escolha == 2:
            matriz_transposta()
        elif escolha == 3:
            multiplicacao()
        elif escolha == 4:
            soma()
        else:
            continue

        request = input('Você quer continuar resolvendo? S/N? ').strip().upper()
        if request in ['NAO', 'N']:
            break

# Função para obter e validar a opção do usuário
def getopcao():
    while True:
        try:
            # Pede ao usuário para escolher uma operação
            opcao = int(input('Qual Operação você quer Fazer? \n1- Calculo de matriz\n2- Matriz transposta\n3- Multiplicação\nEscolha: '))
            
            # Verifica se a opção está entre as válidas (1, 2, 3 ou 4)
            if opcao not in [1, 2, 3, 4]:
                raise ValueError()  # Gera erro se a opção não está entre 1, 2 ou 3
            return opcao
        except ValueError:
            print('Por favor, informe um valor numérico entre 1 e 3.')

# Função para calcular a solução de um sistema de equações lineares
def calculo_de_matriz():
    # Obter a ordem do sistema de equações (número de variáveis)
    ordem = int(input("Digite a ordem do sistema (número de variáveis, ex: 2 para x e y): "))
    
    matriz = []
    print(f"Insira os coeficientes das equações na forma: a1x1 + a2x2 + ... + anxn = c (ordem {ordem})")
    print("Você pode usar frações (ex: 1/2), números negativos e 0 para termos que não aparecem.")

    # Coleta os coeficientes e termos independentes para cada equação
    for i in range(ordem):
        equacao = input(f"Digite os coeficientes e o termo independente da equação {i+1} (formato: a1 a2 ... an c): ")
        
        # Converte cada entrada em Fraction para lidar com frações e números decimais
        coef = [float(Fraction(x)) for x in equacao.split()]
        matriz.append(coef)

    # Separa a matriz de coeficientes (primeiros 'ordem' valores) e o vetor do lado direito (último valor de cada linha)
    coeficientes = np.array([linha[:ordem] for linha in matriz])
    lado_direito = np.array([linha[ordem] for linha in matriz])

    # Tenta resolver o sistema de equações lineares usando o método NumPy
    try:
        solucao = np.linalg.solve(coeficientes, lado_direito)
        print(f"Valores das variáveis: {solucao}")
    except np.linalg.LinAlgError as e:
        print(f"Erro ao resolver o sistema: {e}")

# Função para calcular a transposta de uma matriz
def matriz_transposta():
    # Recebe o número de linhas e colunas da matriz
    R = int(input("Entre o número de linhas: "))
    C = int(input("Entre o número de colunas: "))
    print("Coloque os valores em uma única linha separadamente (Separado por espaço): ")
    
    # Coleta todos os valores da matriz em uma única linha
    entradas = list(map(int, input().split()))

    # Converte a lista de entradas para uma matriz NumPy com a forma especificada
    matriz = np.array(entradas).reshape(R, C)
    print("Matriz original:")
    print(matriz)

    # Calcula a matriz transposta
    transposta_np = matriz.T
    print("Matriz transposta:")
    print(transposta_np)

# Função para multiplicar duas matrizes
def multiplicacao():
    # Solicita os valores para a primeira matriz
    print("Informe o valor da primeira matriz:")
    R = int(input("Entre o número de linhas: "))
    C = int(input("Entre o número de colunas: "))
    print("Coloque os valores em uma única linha separadamente (Separado por espaço): ")
    entradas = list(map(int, input().split()))

    # Cria a primeira matriz a partir das entradas
    matriz = np.array(entradas).reshape(R, C)
    print("Primeira matriz:")
    print(matriz)

    # Solicita os valores para a segunda matriz
    print("Informe o valor da segunda matriz:")
    R2 = int(input("Entre o número de linhas: "))
    C2 = int(input("Entre o número de colunas: "))
    print("Coloque os valores em uma única linha separadamente (Separado por espaço): ")
    entradas2 = list(map(int, input().split()))

    # Cria a segunda matriz a partir das entradas
    matriz2 = np.array(entradas2).reshape(R2, C2)
    print("Segunda matriz:")
    print(matriz2)

    # Verifica se é possível realizar o produto das matrizes (número de colunas da primeira deve ser igual ao número de linhas da segunda)
    if C != R2:
        print("Erro: o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    else:
        # Calcula o produto das matrizes
        resultado = np.matmul(matriz, matriz2)
        print("Resultado do produto das matrizes:")
        print(resultado)

def soma():
    # Solicita os valores para a primeira matriz
    print("Informe o valor da primeira matriz:")
    R = int(input("Entre o número de linhas: "))
    C = int(input("Entre o número de colunas: "))
    print("Coloque os valores em uma única linha separadamente (Separado por espaço): ")
    entradas = list(map(int, input().split()))

    # Cria a primeira matriz a partir das entradas
    matriz = np.array(entradas).reshape(R, C)
    print("Primeira matriz:")
    print(matriz)

    # Solicita os valores para a segunda matriz
    print("Informe o valor da segunda matriz:")
    R2 = int(input("Entre o número de linhas: "))
    C2 = int(input("Entre o número de colunas: "))
    print("Coloque os valores em uma única linha separadamente (Separado por espaço): ")
    entradas2 = list(map(int, input().split()))

    # Cria a segunda matriz a partir das entradas
    matriz2 = np.array(entradas2).reshape(R2, C2)
    print("Segunda matriz:")
    print(matriz2)

    # Verifica se é possível realizar o produto das matrizes (número de colunas da primeira deve ser igual ao número de linhas da segunda)
    if C != R2:
        print("Erro: o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    else:
        resultado = np.sum([matriz, matriz2], axis=0)
        print("Resultado do produto das matrizes:")
        print(resultado)  

main()
