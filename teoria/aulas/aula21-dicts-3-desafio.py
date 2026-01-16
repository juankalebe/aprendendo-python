i=0
lista_pessoas=[]

while i<5:
    verif = input(f"Deseja inserir um novo produto [s ou n]? ")
    if verif == "s":
        i += 1
    else:
        break

    print("Produto ",i,": ")
    pessoa = {} # importante deixar essa criação aqui dentro do laço, senão ele fica se sobreescrevendo depois
    pessoa["id"] = int(input(f"Insira o id: "))
    pessoa["nome"] = input(f"Insira o nome do produto: ")
    pessoa["preco"] = float(input(f"Insira o preço: "))
    lista_pessoas.append(pessoa) # adicionando o dict à lista

    print(f"\nQuantidade de produtos cadastrados: {i}")
    j=1
    for pessoa in lista_pessoas:
        print(f"Produto {j}:")
        for chave in pessoa:
            print(f"{chave.title()}: {pessoa[chave]}")
        j+=1
        print() # pular linha a cada pessoa
