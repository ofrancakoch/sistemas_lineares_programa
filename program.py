def solver(system_size : int, system : list):
    Size = int(input("Enter the System Size:"))
    print("Enter the coeficients")
    coeficients = []
    for coeficient in range(Size):
        coeficients.append(float(input()))
    print(coeficients)
        
    # Initialize matrix
    matrix = []
    print("Enter the entries row wise:")

    # For user input
    # A for loop for row entries
    for row in range(Size+1):    
        a = []
        # A for loop for column entries
        for column in range(Size+1):   
            a.append(int(input()))
        matrix.append(a)

    # For printing the matrix
    for row in range(Size):
        for column in range(Size):
            print(matrix[row][column], end=" ")
        print()



def introduction():
    pass



def conclusion(system : list):
    pass