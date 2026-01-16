# Declare quatro variáveis: id (tipo int), nome (tipo str), salário (tipo float) e brasileiro (tipo bool)
# Peça para que o usuário informe os dados acima e ao final imprima tudo com o linguição (separando com virgulas) 
# e com o f-string

id = int(input("id: "))
nome = input("Nome: ")
salario = float(input("Salário: "))
brasileiro = bool(input("Brasileiro (true ou false): "))
# Em Python, qualquer string que não esteja vazia ("") avalia como True em um contexto booleano
# Por isso mesmo escrevendo False ou 0 ela está retornando True. Por isso para fazer corretamente 
# Você deve usar if para validar depois

print("id: ",id,"\nNome: ",nome,"\nSalário: ",salario,"\nBrasileiro: ",brasileiro) # linguicao

print(f"id: {id}\nNome: {nome}\nSalário: {salario:.2f}\nBrasileiro: {brasileiro}") # f-string