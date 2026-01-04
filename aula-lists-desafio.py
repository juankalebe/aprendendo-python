'''
DESAFIO 1
Listas (lists) [Curso de Python: Aula 16]
'''

lista = []
control = 1
i=0
while control != 0:
    control = int(input(f"Elemento inteiro {i}: "))
    if control != 0:
        lista.append(control)        
        i+=1

lista.sort()
print(lista)
print(f"Foram adicionados {i} elementos. O menor elemento foi o {lista[0]} e o maior foi o {lista[i-1]}")