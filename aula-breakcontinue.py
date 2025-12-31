'''for i in range(1,11):
    if i == 5:
        continue # nao vai imprimir o 5
    print(i, "",end="")

for i in range(1,11):
    if i == 5:
        break # o vai imprimir até o 4
    print(i, "",end="")'''

'''Crie um programa que mostre na tela um contador.
O contador deve ser inicializado com zero. O usuário deve ter 
a opção de incrementar uma unidade ao contador ou de encerrar
o programa. Enquanto o usuário continuar decidindo incrementar o contador,
o programa não deve ser encerrado. O programa encerra quando
o usuário decidir. Utilize um laço com os comandos continue
e break'''

incrementar = True
contador = 0
while incrementar == True:
    print("Contador: ",contador)
    incrementar = int(input("Deseja incrementar? [1 = true ou 0 = false]" ))
    contador += 1
# nao vi necessidade de usar o break ou o continue. Só se tivesse usando o for
# fugindo da ideia de não parar enquanto o usuário quiser continuar, ou seja, teria um limite
