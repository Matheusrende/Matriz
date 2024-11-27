import unittest
import numpy as np
from fractions import Fraction

# Funções do código fornecido
def soma(matriz1, matriz2):
    # Função modificada para aceitar entradas como parâmetros
    R, C = matriz1.shape
    R2, C2 = matriz2.shape

    if R != R2 or C != C2:
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
    
    return np.add(matriz1, matriz2)

def calculo_de_matriz(coeficientes, lado_direito):
    try:
        solucao = np.linalg.solve(coeficientes, lado_direito)
        return solucao
    except np.linalg.LinAlgError as e:
        return str(e)

def matriz_transposta(matriz):
    return matriz.T

# Classe de testes
class TestOperations(unittest.TestCase):
    def test_soma(self):
        # Teste para soma de matrizes
        matriz1 = np.array([[1, 2], [3, 4]])
        matriz2 = np.array([[5, 6], [7, 8]])
        resultado_esperado = np.array([[6, 8], [10, 12]])
        resultado = soma(matriz1, matriz2)
        np.testing.assert_array_equal(resultado, resultado_esperado)

        # Teste com matrizes de dimensões incompatíveis
        matriz3 = np.array([[1, 2]])
        with self.assertRaises(ValueError):
            soma(matriz1, matriz3)

    def test_calculo_de_matriz(self):
        # Teste para cálculo de matriz (solução de sistema linear)
        coeficientes = np.array([[3, -2], [1, 1]])
        lado_direito = np.array([5, 5])
        resultado_esperado = np.array([3, 2])
        resultado = calculo_de_matriz(coeficientes, lado_direito)
        np.testing.assert_array_equal(resultado, resultado_esperado)

        # Teste para sistema sem solução
        coeficientes2 = np.array([[1, 1], [1, 1]])
        lado_direito2 = np.array([1, 2])
        resultado = calculo_de_matriz(coeficientes2, lado_direito2)
        self.assertEqual(resultado, 'Singular matrix')

    def test_matriz_transposta(self):
        # Teste para matriz transposta
        matriz = np.array([[1, 2], [3, 4]])
        resultado_esperado = np.array([[1, 3], [2, 4]])
        resultado = matriz_transposta(matriz)
        np.testing.assert_array_equal(resultado, resultado_esperado)

        # Teste com matriz 1x1
        matriz2 = np.array([[5]])
        resultado_esperado2 = np.array([[5]])
        resultado2 = matriz_transposta(matriz2)
        np.testing.assert_array_equal(resultado2, resultado_esperado2)

# Executar os testes
if __name__ == '__main__':
    unittest.main()
