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
            Pedrapapel()
        else:
            continue
        
        request = input('Você quer continuar jogando? S/N? ').upper()
        if request in ['NAO','N']:
            break

def getopcao():
    try:
        opcao = input('Qual jogo você quer jogar? \n 1- Jogo da velha?\n 2- Bola magica\n 3- Pedra papel e tesoura')
        if opcao not in [1,2,3]:
                    raise Exception()
    except (ValueError,Exception):
        print('please Enter a Value 1 or 2')
        
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
    # Define a matriz original
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Converte a lista de listas em uma matriz NumPy
    matriz_np = np.array(matriz)

    # Calcula a matriz transposta
    transposta_np = matriz_np.T

    # Imprime a matriz transposta
    print("Matriz transposta:")
    print(transposta_np)



    