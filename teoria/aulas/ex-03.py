'''Faça um programa que receba o salário de um funcionário e o percentual de aumento, 
calcule e mostre o valor do aumento e o novo salário.'''

salario = float(input("Salário: "))
perc_aum = float(input("Percentual de aumento: ")) / 100.0

print(f"Valor de aumento: R${perc_aum*salario:.2f}\nNovo salário: R${salario + perc_aum*salario:.2f}")