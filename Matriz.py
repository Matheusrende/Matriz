import numpy as np
from fractions import Fraction
 
def main():
    while True:

        escolha = getopcao()
        if escolha == 1 :
            calculo_de_matriz()
        elif escolha == 2 :
            matriz_transposta()
        elif escolha == 3 :
            multiplicacao()
        else:
            continue
        
        request = input('Você quer continuar jogando? S/N? ').upper()
        if request in ['NAO','N']:
            break

def getopcao():
    try:
        opcao = input('Qual Operação você quer Fazer? \n 1- Calculo de matriz?\n 2- Uma matriz transposta?\n 3- Multiplicação?')
        if opcao not in [1,2,3]:
                    raise Exception()
    except (ValueError,Exception):
        print('Por favor informe um valor de 1 a 3')
        
    else : 
        return opcao


# Função para receber a ordem da matriz e os coeficientes do usuário
def calculo_de_matriz():
    # Obter a ordem do sistema de equações (número de variáveis)
    ordem = int(input("Digite a ordem do sistema (número de variáveis, ex: 2 para x e y): "))
    
    matriz = []
    print(f"Insira os coeficientes das equações na forma: a1x1 + a2x2 + ... + anxn = c (ordem {ordem})")
    print("Você pode usar frações (ex: 1/2), números negativos e 0 para termos que não aparecem.")

    for i in range(ordem):  # Para 'ordem' equações
        equacao = input(f"Digite os coeficientes e o termo independente da equação {i+1} (formato: a1 a2 ... an c): ")
        
        # Converte cada entrada em Fraction para lidar com frações e números decimais
        coef = [float(Fraction(x)) for x in equacao.split()]
        matriz.append(coef)

    coeficientes = np.array([linha[:ordem] for linha in matriz])  # Primeiros 'ordem' valores
    lado_direito = np.array([linha[ordem] for linha in matriz])  # O último valor (c)

    # Resolver o sistema de equações lineares
    try:
        solucao = np.linalg.solve(coeficientes, lado_direito)
        print(f"Valores das variáveis: {solucao}")
    except np.linalg.LinAlgError as e:
        print(f"Erro ao resolver o sistema: {e}")
        

def matriz_transposta():

    R = int(input("Entre o numero de linhas: "))
    C = int(input("Entre o numero de ccolunas: "))

    print("Coloque os valores em uma unica linha separadamente (Separado por espaço): ")
    entradas = list(map(int, input().split()))

    # Imprime a matriz acima
    matriz = np.array(entradas).reshape(R, C)
    print(matriz)

    # Converte a lista de listas em uma matriz NumPy
    matriz_np = np.array(matriz)

    # Calcula a matriz transposta
    transposta_np = matriz_np.T

    # Imprime a matriz transposta
    print("Matriz transposta:")
    print(transposta_np)
    
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

    # Verifica se é possível realizar o produto das matrizes
    if C != R2:
        print("Erro: o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    else:
        # Calcula o produto das matrizes
        resultado = np.matmul(matriz, matriz2)
        print("Resultado do produto das matrizes:")
        print(resultado)



    