'''Pode ser assim:
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''

mat = []

mat.append([1,2,3])
mat.append([4,5,6])
mat.append([7,8,9])

#impressao da primeira linha

print("Impressão da primeira linha")
for i in range(3):
    print(mat[0][i],end=" ")
print()

print("Impressão da primeira linha")
for i in mat[0]:
    print(i,end=" ")
print()

print("Impressão da matriz completa")
for i in range(3):
    for j in range (3):
        print(mat[i][j],end=" ")
    print()

print("Impressão da matriz completa")
for linha in mat: #acho que aqui é bom pra entender como funciona. Daí entende como o for anda em lista e em matriz
    for elem in linha:
        print(elem,end=" ")
    print()