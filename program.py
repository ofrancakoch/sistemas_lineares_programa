class SistemaLinear: 
    def __init__(self): 
        self.tamanho = int(input("Insira o tamanho do Sistema Linear: ")) 
        self.matriz = self.get_matriz() 
        self.variaveis = self.get_variaveis()

    def get_matriz(self): 
        # Inicializa a matriz 
        matriz = [] 
        print("Insira os elementos da matriz com o termo independente ao final de cada linha:") 

        for _ in range(self.tamanho):     
            line = [float(input()) for _ in range(self.tamanho + 1)]
            matriz.append(line) 

        return matriz

    def get_variaveis(self):
        print("Insira as variáveis:") 
        variaveis = [str(input()) for _ in range(self.tamanho)]
        return variaveis

    def solver(self): 
        # Criar uma cópia da matriz para não alterar a original
        matriz = [linha[:] for linha in self.matriz]
        tamanho = self.tamanho 
        linha = 0 
        coluna = 0

        while linha < tamanho and coluna < tamanho: 
            diagonal = matriz[linha][coluna]

            if diagonal != 0:
                for r in range(linha + 1, tamanho):
                    if matriz[r][coluna] != 0:
                        pivot = -matriz[r][coluna] / diagonal
                        for c in range(coluna, tamanho + 1):
                            matriz[r][c] += pivot * matriz[linha][c]

                linha += 1
                coluna += 1
            
            else:
                # Troca de linhas caso o pivô seja zero
                for r in range(linha + 1, tamanho):
                    if matriz[r][coluna] != 0:
                        matriz[linha], matriz[r] = matriz[r], matriz[linha]
                        break

            # Verificar SPI e SI
            for i in range(tamanho):
                if all(matriz[i][j] == 0 for j in range(tamanho)) and matriz[i][tamanho] != 0:
                    raise ValueError("Sistema Impossível (SI): Nenhuma Solução.")
                elif all(matriz[i][j] == 0 for j in range(tamanho)) and matriz[i][tamanho] == 0:
                    raise ValueError("Sistema Possível e Indeterminado (SPI): Infinitas Soluções.")
                    
        return matriz

    def resultado(self):
        # Substituição regressiva para encontrar os valores das variáveis
        matriz = self.solver()
        tamanho = self.tamanho
        resultado = [0 for _ in range(tamanho)]

        for i in range(tamanho - 1, -1, -1):
            soma = sum(matriz[i][j] * resultado[j] for j in range(i + 1, tamanho))
            resultado[i] = (matriz[i][tamanho] - soma) / matriz[i][i]

        return resultado
    

    def mostrarSL(self, matriz):
        variaveis = self.variaveis
        
        for linha in range(self.tamanho):
            partes_equacao = []
            for col in range(self.tamanho):
                coef = round(matriz[linha][col], 2)
                if coef != 0:
                    partes_equacao.append(f"{coef}{variaveis[col]}")
            
            resultado = round(matriz[linha][self.tamanho], 2)
            equacao_str = " + ".join(partes_equacao).replace("+ -", "- ")
            print(equacao_str, "=", resultado)

    def printResultados(self):
        print("\n\nSistema Original\n")
        self.mostrarSL(self.matriz)
        print("\nSistema Escalonado\n")
        self.mostrarSL(self.solver())
        print("\nResultado\n")
        solucao = self.resultado()
        for var, sol in zip(self.variaveis, solucao):
            print(f"{var} = {sol:.2f}")
        print()

# Execução do programa
if __name__ == "__main__":
    executar = SistemaLinear()
    executar.printResultados()
