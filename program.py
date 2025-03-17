class LinearSystems: 
    def __init__(self): 
        self.size = int(input("Enter the size of the linear system: ")) 
        self.matriz = self.get_matriz() 
        self.variables = self.get_variables()

    def get_matriz(self): 
        # Inicializa a matriz 
        matriz = [] 
        print("Enter the entries row-wise:") 

        for _ in range(self.size):     
            line = [float(input()) for _ in range(self.size + 1)]
            matriz.append(line) 

        return matriz

    def get_variables(self):
        print("Enter the variables:") 
        variables = [str(input()) for _ in range(self.size)]
        return variables

    def solver(self): 
        # Criar uma cópia da matriz para não alterar a original
        matriz_unsolved = [row[:] for row in self.matriz]
        size = self.size 
        row = 0 
        column = 0

        while row < size and column < size: 
            diagonal_element = matriz_unsolved[row][column]

            if diagonal_element != 0:
                for r in range(row + 1, size):
                    if matriz_unsolved[r][column] != 0:
                        pivot = -matriz_unsolved[r][column] / diagonal_element
                        for c in range(column, size + 1):
                            matriz_unsolved[r][c] += pivot * matriz_unsolved[row][c]

                row += 1
                column += 1
            
            else:
                # Troca de linhas caso o pivô seja zero
                for r in range(row + 1, size):
                    if matriz_unsolved[r][column] != 0:
                        matriz_unsolved[row], matriz_unsolved[r] = matriz_unsolved[r], matriz_unsolved[row]
                        break
                else:
                    column += 1  # Pula a coluna se não houver elementos não nulos

            # Verificar SPI e SI
            for i in range(size):
                if all(matriz_unsolved[i][j] == 0 for j in range(size)) and matriz_unsolved[i][size] != 0:
                    raise ValueError("Sistema Impossível (SPI): Nenhuma solução existe.")
                elif all(matriz_unsolved[i][j] == 0 for j in range(size)) and matriz_unsolved[i][size] == 0:
                    raise ValueError("Sistema Indeterminado (SI): Infinitas soluções.")

        return matriz_unsolved

    def back_substitution(self):
        # Substituição regressiva para encontrar os valores das variáveis
        matriz = self.solver()
        size = self.size
        resultado = [0 for _ in range(size)]

        for i in range(size - 1, -1, -1):
            sum_ax = sum(matriz[i][j] * resultado[j] for j in range(i + 1, size))
            resultado[i] = (matriz[i][size] - sum_ax) / matriz[i][i]

        return resultado
    

    def printSistemaLinear(self, matriz):
        variables = self.variables
        
        for row in range(self.size):
            equation_parts = []
            for col in range(self.size):
                coef = round(matriz[row][col], 2)
                if coef != 0:
                    equation_parts.append(f"{coef}{variables[col]}")
            
            result = round(matriz[row][self.size], 2)
            equation_str = " + ".join(equation_parts).replace("+ -", "- ")
            print(equation_str, "=", result)

    def resultado(self):
        print("Sistema Original\n")
        self.printSistemaLinear(self.matriz)
        print("\nSistema Escalonado\n")
        self.printSistemaLinear(self.solver())
        print("\nResultado\n")
        solution = self.back_substitution()
        for var, sol in zip(self.variables, solution):
            print(f"{var} = {sol:.2f}")

# Execução do programa
if __name__ == "__main__":
    teste = LinearSystems()
    teste.resultado()
