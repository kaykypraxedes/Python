import numpy as np

def CriaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"{i+1}, {j+1}: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matriz)


def main():
    n = int(input("Insira qual o o numero de variaveis do sistema: "))
    A = CriaMatriz(n, n)
    b = CriaMatriz(n, 1)
    print("Matriz A:")
    print(A)
    print("Vetor b:")
    print(b)
