pessoa = {
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}

print(f"Nome: {pessoa["nome"]}\nPeso: {pessoa["peso"]}\nIdade: {pessoa["idade"]}")

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print(f"\nNome: {pessoa["nome"]}\nPeso: {pessoa["peso"]}\nIdade: {pessoa["idade"]}")

for chave in pessoa: #aprendi que assim a var chave vai retornar o nome de cada chave
    if isinstance(pessoa[chave], str):
        #essa funçao serve para eu verificar se o tipo da variável que eu peguei é do tipo que eu defini no segundo parâmetro
        pessoa[chave] = input(f"Insira o {chave}: ")
        #já que chave retorna o nome da chave da vez, então fica útil para colocar no texto direto
    elif isinstance(pessoa[chave],int):
        pessoa[chave] = int(input(f"Insira o {chave}: "))
    elif isinstance(pessoa[chave],float):
        pessoa[chave] = float(input(f"Insira o {chave}: "))

for chave in pessoa:
    print(f"{chave.title()}: {pessoa[chave]}")
    #esse title serve para deixar a primeira letra da string em maiúsculo