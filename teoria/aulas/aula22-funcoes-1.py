'''
Crie um programa para definir e executar uma função que recebe dois números como parâmetro e retorna o maior entre os dois
Docstring for aula21-funcoes-1
'''

def maior_de2 (A, B): # variaveis no escopo local apenas
    if A > B:
        return A
    else:
        return B
    
a = int(input("a: "))
b = int(input("b: "))

print("Maior: ",maior_de2(a,b))