class LinearSystems: 
    def __init__(self): 
        self.size = int(input("Enter the size of the linear system: ")) 
        self.matrix = self.get_matrix() 
        self.variables = self.get_variables()

    def get_matrix(self): 
        # Inicializa a matriz 
        matrix = [] 
        print("Enter the entries row-wise:") 

        for _ in range(self.size):     
            line = [float(input()) for _ in range(self.size + 1)]
            matrix.append(line) 

        return matrix

    def get_variables(self):
        print("Enter the variables:") 
        variables = [str(input()) for _ in range(self.size)]
        return variables

    def solver(self): 
        # Criar uma cópia da matriz para não alterar a original
        matrix_unsolved = [row[:] for row in self.matrix]
        size = self.size 
        row = 0 
        column = 0

        while row < size and column < size: 
            diagonal_element = matrix_unsolved[row][column]

            if diagonal_element != 0:
                for r in range(row + 1, size):
                    if matrix_unsolved[r][column] != 0:
                        pivot = -matrix_unsolved[r][column] / diagonal_element
                        for c in range(column, size + 1):
                            matrix_unsolved[r][c] += pivot * matrix_unsolved[row][c]

                row += 1
                column += 1

            else:
                # Troca de linhas caso o pivô seja zero
                for r in range(row + 1, size):
                    if matrix_unsolved[r][column] != 0:
                        matrix_unsolved[row], matrix_unsolved[r] = matrix_unsolved[r], matrix_unsolved[row]
                        break
                else:
                    column += 1  # Pula a coluna se não houver elementos não nulos

        return matrix_unsolved

    def printMatrix(self): 
        matrix = self.solver()
        print("Matrix after Gaussian elimination:")
        for row in matrix:
            print(" ".join(map(str, row)))

teste = LinearSystems()
teste.printMatrix()
