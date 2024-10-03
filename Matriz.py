import numpy as np
from fractions import Fraction

# Função para receber a ordem da matriz e os coeficientes do usuário
def obter_matriz(ordem):
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
    
    return coeficientes, lado_direito

# Obter a ordem do sistema de equações (número de variáveis)
ordem = int(input("Digite a ordem do sistema (número de variáveis, ex: 2 para x e y): "))

# Obter a matriz de coeficientes e o vetor do lado direito
coeficientes, lado_direito = obter_matriz(ordem)

try:
    solucao = np.linalg.solve(coeficientes, lado_direito)
    print(f"Valores das variáveis: {solucao}")
except np.linalg.LinAlgError as e:
    print(f"Erro ao resolver o sistema: {e}")
    
    #alo
