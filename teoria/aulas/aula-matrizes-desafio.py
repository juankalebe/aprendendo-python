mat = [] #criando assim ela tem tamanho 0 - nenhum índice

print("Preenchimento da matriz completa")
for i in range(3):
    linha1=[] #cria uma linha para poder adicionar elementos
    for j in range (4):
        linha1.append(int(input(f"Elemento {i+1}x{j+1}: ")))
    mat.append(linha1) #adiciona uma linha como um elemento à lista original, criando então matriz
    print()

print("Impressão da matriz completa")
for linha in mat: #acho qu1e aqui é bom pra entender como funciona. Daí entende como o for anda em lista e em matriz
    for elem in linha:
        print(elem,end=" ")
    print()

maior=mat[0][0]
menor=maior
index_linha_maior = 0
index_coluna_maior = 0
index_linha_menor = 0
index_coluna_menor = 0

for linha in range(3):
    for coluna in range(4):
        if mat[linha][coluna] > maior:
            maior = mat[linha][coluna]
            index_linha_maior = linha
            index_coluna_maior = coluna
        elif mat[linha][coluna] < menor:
            menor = elem
            index_linha_menor = linha
            index_coluna_menor = coluna

print(f"Maior: {maior} índice: {index_linha_maior+1}x{index_coluna_maior+1}\tMenor: {menor} índice: {index_linha_menor+1}x{index_coluna_menor+1}")