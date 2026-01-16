'''
Crie uma lista com os valores 10, 20 e 30. Em seguida, imprima o conteúdo e o id() da lista. 
Depois adicione o elemento 40 ao fim da lista e altere o conteúdo do primeiro elemento para 0. 
Imprima novamente o conteúdo e o id() da lista
'''
lista = [10,20,30] # aqui é uma lista, então é um objeto mutável
print(f"Valor = {lista} e ID = {id(lista)}") # dá o endereço de memória
lista.append(40)
lista[0]=0
print(f"Valor = {lista} e ID = {id(lista)}") # dá o mesmo ID de antes