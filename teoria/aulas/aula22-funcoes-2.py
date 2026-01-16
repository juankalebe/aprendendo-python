'''
Crie um programa para definir e executar uma função que recebe uma lista de inteiros como parâmetro e imprime na tela o quadrado de cada um dos elementos da lista
'''

def quadrado_lista (lista): # é um caso de uma função sem retorno
    for elem in lista:
        print(elem**2,end=" ")

    

lista_inteiros = [1,5,6,8,6,2,1,5]
quadrado_lista(lista_inteiros)
print()
