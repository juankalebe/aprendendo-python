'''
Crie uma variável simples e atribua o conteúdo 5 a ela. Em seguida imprima o conteúdo e o id() da variável. 
Depois altere o conteúdo da variável para 10 e imprima novamente o conteúdo e o id() da variável
'''
a = 5 # aqui é um número, então é um objeto imutável
print(f"Valor = {a} e ID = {id(a)}") # dá o endereço de memória
a = 10
print(f"Valor = {a} e ID = {id(a)}") # dá um ID diferente do anterior. Ou seja, o objeto anterior foi destruído