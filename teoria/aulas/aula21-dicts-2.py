lista_pessoas=[] # criando lista que irá armazenar as dicts

for _ in range(3): #esse "_" é uma convenção em python para quando o valor que a var assumir não será usado
    pessoa = {}
    pessoa["nome"] = input(f"Insira o nome: ")
    pessoa["peso"] = float(input(f"Insira o peso: "))
    pessoa["idade"] = int(input(f"Insira a idade: "))
    lista_pessoas.append(pessoa) # adicionando o dict à lista
print() # pular linha antes de printar
for pessoa in lista_pessoas:
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa[chave]}")
        #esse title serve para deixar a primeira letra da string em maiúsculo
    print() # pular linha a cada pessoa
