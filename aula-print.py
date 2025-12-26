print( "Olá, seja bem vindo(a)")

print( "O valor inteiro é:",10)
print( f"O valor inteiro é: {10:d}") #imprimir em decimal
print( f"O valor inteiro é: {10:b}") #imprimir em binário


print( f"O valor de Pi é: {3.14159265:.8f}") #imprimir decimal completo (por padrão só até 6 após a vírgula)
print( f"O valor de Pi é: {3.14159265:.2f}") #imprimir decimal só com duas casas decimais


# Crie um programa que imprima na tela o nome, a idade, o salário e a
# nacionalidade de uma pessoa. Você deve imprimir tas dados utilizando
# formatação por meio de f-strings. Utilize caracteres de escape para
# melhor organizar sua formatação
print(f"\tDADOS DA PESSOA\n\tNOME:\t\tJOÃO KLEBER\n\tIDADE:\t\t{25:d} ANOS\n\tSALÁRIO:\tR${4000: .2f}\n\tNACIONALIDADE:\tBRASILEIRO")