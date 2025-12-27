# Crie um programa que peça ao usuário para informar três números com casas decimais. 
# Calcule a média entre os três números e mostre o resultado na tela, formatado para 
# apresentar duas casas decimais.

media = (float(input("Número 1: ")) + float(input("Número 2: ")) + float(input("Número 3: "))) / 3

print(f"Média: {media: .2f}\n")