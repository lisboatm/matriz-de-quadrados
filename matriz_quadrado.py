def main():
    # Número de matrizes
    n_matrizes = int(input())
    
    for k in range(n_matrizes):
        # Dimensão da matriz
        n = int(input())
        matriz = []
        max_digits = [0] * n
        
        # Leitura da matriz e cálculo dos quadrados
        for i in range(n):
            row = list(map(int, input().split()))
            matriz.append(row)
            for j in range(n):
                # Calcular o quadrado
                row[j] = row[j] ** 2
                # Determinar o número de dígitos do maior número em cada coluna
                max_digits[j] = max(max_digits[j], len(str(row[j])))
        
        # Imprimir o cabeçalho da matriz
        if k > 0:
            print()
        print(f"Quadrado da matriz #{k + 4}:")
        
        # Imprimir a matriz formatada
        for i in range(n):
            for j in range(n):
                # Imprimir cada número com o alinhamento correto
                print(f"{matriz[i][j]:>{max_digits[j]}}", end=' ' if j < n - 1 else '\n')

if __name__ == "__main__":
    main()
