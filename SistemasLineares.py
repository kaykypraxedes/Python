import numpy as np

def printMatrizes(prim, seg, res):
    n = len(prim)
    for i in range(n):
        vezes = "." if i == int (n / 2) else " "
        linha_prim = " ".join(f"{elem:6.2f}" for elem in prim[i])
        linha_prim = f"|{linha_prim}| {vezes} "
        if seg is not None:
            linha_seg = " ".join(f"{elem:6.2f}" for elem in seg[i])
            linha_seg = f"|{linha_seg}| {vezes} "
        else:
            linha_seg = ""
        linha_res = f"|{res[i,0]:6.2f}|"
        igual = " = " if i == int (n / 2) else "   "
        print(f"{linha_prim}{linha_seg}|x{i+1}|{igual}{linha_res}")

def CriaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"{i+1}, {j+1}: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matriz)

def EliminacaoDeGauss(A, b):
    n = len(A)
    U = np.zeros((n, n))
    d = np.zeros((n, 1))
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][i] == 0:
                raise ValueError("Divisão por zero detectada!")
            fator = A[j][i] / A[i][i]
            U[j] = A[j] - fator * A[i]
            d[j] = b[j] - fator * b[i]
    print("\nUx = d:")
    printMatrizes(U, None, d)

def main():
    n = int(input("Insira qual o o numero de variaveis do sistema: "))
    A = CriaMatriz(n, n)
    b = CriaMatriz(n, 1)
    print("\nAx = b:")
    printMatrizes(A, None, b)
    EliminacaoDeGauss(A, b)

if __name__ == "__main__":
    main()