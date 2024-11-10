### README - Desafio F: Matriz de Quadrados

---

#### Descrição do Problema

Atrapalhilton é um estudante muito dedicado, mas um tanto atrapalhado. Seu professor de Matemática, Sr. Sabetudilton, passou uma lista de exercícios para calcular o quadrado de matrizes. No entanto, Atrapalhilton entendeu errado o enunciado e calculou o "quadrado" de uma matriz como sendo a **matriz dos quadrados dos seus elementos**.

Por exemplo:
Para ele, o quadrado da matriz
```
1 3
5 7
```
não é:
```
16 24
40 64
```
mas sim:
```
1 9
25 49
```

Como ele não conseguiu calcular todos os exercícios, ele decidiu escrever um programa que fizesse o trabalho por ele.

---

#### Entrada

- A primeira linha contém um inteiro positivo `N` (`N ≤ 100`), indicando o número de matrizes.
- Para cada matriz:
  - A primeira linha contém um inteiro `M` (`1 ≤ M ≤ 20`), representando o número de linhas e colunas (a matriz é quadrada).
  - Seguem-se `M` linhas, cada uma contendo `M` inteiros `aij` (`0 ≤ aij ≤ 2^32 - 1`), representando os elementos da matriz.

---

#### Saída

- Para cada matriz, imprima o cabeçalho:
  ```
  Quadrado da matriz #x:
  ```
  onde `x` começa em 4, pois Atrapalhilton já havia calculado os quadrados das três primeiras matrizes.
- Imprima a "matriz dos quadrados" formatada, com os números alinhados à direita, de forma que os números em cada coluna fiquem alinhados.
- Deve haver **uma linha em branco entre as saídas de matrizes consecutivas**.

---

#### Exemplo de Entrada
```
1
2
7 12
1024 1
```

#### Exemplo de Saída
```
Quadrado da matriz #4:
  49  144
1048576    1
```

---

### Código Utilizado

```python
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
```

---

### Explicação do Código

1. **Entrada**:
   - Lemos o número de matrizes (`n_matrizes`).
   - Para cada matriz:
     - Lemos o tamanho (`n`).
     - Lemos os elementos da matriz e calculamos o quadrado de cada um.
     - Armazenamos o número de dígitos do maior elemento de cada coluna para garantir o alinhamento.

2. **Processamento**:
   - Calculamos o quadrado de cada elemento da matriz.
   - Garantimos que os números em cada coluna sejam impressos com alinhamento à direita.

3. **Saída**:
   - Imprimimos o cabeçalho da matriz.
   - Imprimimos cada linha da matriz com os valores alinhados corretamente.
   - Adicionamos uma linha em branco entre diferentes matrizes.

---

### Complexidade e Considerações

A complexidade do algoritmo é `O(N * M^2)`, o que é suficiente para os limites do problema (`N ≤ 100` e `M ≤ 20`). Este código foi desenvolvido para atender aos requisitos de formatação exigidos pelo problema.

---

### Instruções para Execução

Para executar o código, salve-o em um arquivo `matriz_quadrado.py` e execute no terminal:

```bash
python3 matriz_quadrado.py
```

Insira os dados conforme o formato descrito na seção de entrada e verifique se a saída está de acordo com o exemplo fornecido.

--- 

### Observações Finais

Este código foi utilizado para resolver o Desafio F na plataforma Beecrowd e passou por testes que garantiram a correta formatação da saída. Se houver problemas de apresentação, verifique os espaçamentos e o alinhamento na sua execução.
