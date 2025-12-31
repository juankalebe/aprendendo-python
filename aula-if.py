''' Crie um programa que peça para o usuário o valor de sua nota.
Caso a nota seja maior ou igual a 7.0, então imprima "Aprovado(a)"
na tela

if (float(input("Nota: ")) >= 7.0):
    print("Aprovado(a)")
'''

'''Crie um programa que peça para o usuário o valor de sua nota.
Caso a nota seja menor que 7.0, mas simultaneamente
maior ou igual a 4.0, então imprima "Tem direito a exame!"
na tela

nota = float(input("Nota: "))

if (nota < 7.0 and nota >= 4.0):
    print("Tem direito a exame!")
'''

#Desafio: juntar os enunciados anteriores e também printar reprovado
#para o caso de nota < 4

nota = float(input("Nota: "))

if (nota >= 7.0):
    print("Aprovado(a)")
if (nota < 7.0 and nota >= 4.0):
    print("Tem direito a exame!")
if (nota < 4.0):
    print("Reprovado")