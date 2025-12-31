'''Crie um programa que imprima os números inteiros de 10 a 1.
Ou seja, deve-se imprimir em ordem decrescente, iniciando em 10
e encerrando em 1. Utilize o while'''

'''
i = 10
while i >= 1:
    print(i, " ",end="")
    i-=1
'''

'''Crie um programa que continue pedindo, repetidas vezes, para que
o usuário insira um número qualquer. O programa deve se encerrar somente
quando o usuário inserir o valor zero'''
numero = 1
while numero != 0:
    numero = int(input("Insira um número: "))