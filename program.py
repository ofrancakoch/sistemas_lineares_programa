class linearSystems: 

    def _init_(self): 
        self.size = int(input("Enter the size of the linear system")) 
        self.matrix = self.get_matrix() 
        self.variables = self.get_variables()

    def get_matrix(self): 
        # Initialize matrix 
        matrix = [] 
        print("Enter the entries row wise:") 

        for row in range(self.size):     
            line = [] 
            # A for loop for column entries 
            for column in range(self.size + 1):    
                line.append(int(input())) 
            matrix.append(line) 

        return matrix

    
    def get_variables(self):
        print("Enter the variables") 
        variables = [] 
        for variable in range(self.size): 
            variables.append(float(input())) 
        print(variables) 
        return variables

    def solver(self): 
        matrix_unsolved = self.matrix 
        size = self.size 
        row = 0 
        column = 0
        diagonal_element = matrix_unsolved[row][column]
        while (diagonal_element != None) or ((row < size) and (column < size)): 

            if diagonal_element != 0:

                for r in range(row + 1, size):
                    pivot = -1*diagonal_element/matrix_unsolved[r][column]
                    for c in range(column, size + 1):
                        matrix_unsolved[r][c] = matrix_unsolved[row][c] + pivot*matrix_unsolved[r][c]

                row += 1
                column += 1
                diagonal_element = matrix_unsolved[row][column]
            else:

                for r in range(row + 1, size):
                    if matrix_unsolved[r][column] != 0:
                        wrong_row = matrix_unsolved[row]   
                        matrix_unsolved[row] = matrix_unsolved[r]
                        matrix_unsolved[r] = wrong_row
                #Fazer exceçao para que trate SPI e SI

        return matrix_unsolved

    def printMatrix(self, size, matrix): 
        for row in range(size): 
            for column in range(size+1): 
                print(matrix[row][column], end=" ") 
            print() 

    def conclusion(self, system : list): 

        pass