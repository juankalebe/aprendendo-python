'''
HANDS-ON
Listas (lists) [Curso de Python: Aula 16]
'''

lista = []

for i in range(5):
    lista.append(int(input(f"Elemento inteiro {i}: "))) 
print()
for i in range(5):
    print(lista[i],"",end="") 
#outra forma mais direta
print()
for elem in lista:
    print(elem,"",end="") 

print("\nMédia: ", sum(lista)/5)



