#função abs():
# A função abs() em Python retorna o valor absoluto de 
# um número, transformando números negativos em positivos,
# funcionando para inteiros, floats e até números complexos (retornando sua magnitude)

print(abs(-5))

#função chr():
# A função chr() recebe um valor inteiro e retorna o caractere Unicode correspondente 
# Vai de 0 a 1.114.111 que é o limite da tabela Unicode
# Similar à tabela ASCII, mas com muito mais caracteres
print(chr(102))

#função len():
# Retorna o número de itens (tamanho ou comprimento) 
# de um objeto, como o número de caracteres em uma string
print(len("KALEBE"))

# função max() e min()
# A max() retorna o maior item de um iterável (como uma lista, tupla ou conjunto) 
# ou o maior valor entre vários argumentos fornecidos
# e a min() é justamente o contrário
print(max("KALEBE")) # no caso aqui ele compara pelo código da tabela ASCII / Unicode, mas retorna a letra
print(max(1,25,64,58))
print(min("KALEBE"))
print(min(1,25,64,58))

# função sum()
# Retorna a soma de todos os itens de um iterável (como uma lista, tupla ou conjunto) 
# ou de um conjunto de dados
print(sum([1,1,1,1,1])) # formato: sum(iteravel, start=0). Por isso eu precisei colocar os colchetes para listar os itens

# Função sorted() 
# Ordena os itens de um iterável (como listas, tuplas, dicionários) e 
# retorna uma nova lista ordenada, sem modificar o original, 
# por padrão em ordem crescente, mas pode ser configurada para ordem decrescente
print(sorted([5,4,3,2,1])) # vai printar na ordem crescente

# função range()
# gera uma sequência imutável de números inteiros
# Ela pode receber até três argumentos: 
# start (início, padrão 0), stop (fim, exclusivo - unico que é obrigatório) e 
# step (incremento, padrão 1), e retorna um objeto iterável
print(range(5)) # só printou range (0,5)
print(sorted(range(5))) # printou [0,1,2,3,4]

'''A função enumerate() em Python adiciona um contador (índice) a um iterável 
(como lista, tupla ou string) e retorna um objeto enumerado que produz pares de (índice, valor) 
em cada iteração, simplificando loops for quando você precisa tanto do índice quanto do elemento, 
começando o índice por padrão em 0 e podendo ser customizado com o parâmetro start'''
# Exemplo básico:
frutas = ['maçã', 'banana', 'cereja']
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

'''A função zip() em Python agrega elementos de duas ou mais sequências (listas, tuplas, etc.) 
em pares (ou tuplas de múltiplos elementos) e retorna um iterador que pode ser usado em loops 
ou convertido em uma lista de tuplas, combinando o primeiro item de cada sequência, o segundo 
item de cada uma, e assim por diante, parando quando a menor sequência se esgota'''

'''map() é uma função interna que aplica uma função a cada item de um iterável (como uma lista ou tupla) 
e retorna um objeto map (um iterador) com os resultados'''

'''A função filter() em Python cria um iterador que seleciona elementos de um iterável (como lista, tupla) 
que satisfazem uma condição, retornando apenas os itens para os quais uma função de teste retorna True (verdadeiro) 
ou um valor "truthy" (não-zero, não-falso)'''

'''A função open() em Python serve para abrir arquivos, retornando um objeto de arquivo que permite ler, escrever ou adicionar conteúdo'''

'''A função type() em Python serve para descobrir e retornar o tipo de dado de uma variável ou objeto'''

'''A função id() em Python retorna um identificador inteiro único para um objeto, que representa seu endereço na memória'''

'''A função callable() em Python verifica se um objeto pode ser "chamado" (invocado com parênteses ()), retornando True se for e False caso contrário, sendo útil para validação em tempo de execução'''

'''A função isinstance() em Python verifica se um objeto é uma instância de uma classe específica ou de uma tupla de classes, retornando True se for o caso e False caso contrário'''

'''A função any() em Python verifica se pelo menos um elemento em um iterável é avaliado como True; se encontrar um True, retorna True imediatamente, e se o iterável estiver vazio ou nenhum elemento for True, retorna False'''

'''A função all() em Python verifica se todos os elementos de um iterável são considerados "verdadeiros"; ela retorna True se todos forem verdadeiros ou se o iterável for vazio, e False se encontrar qualquer elemento "falso"'''

'''A função dir() em Python lista os atributos (métodos e variáveis) de um objeto ou os nomes no namespace atual'''

'''A função eval() em Python analisa e executa uma string como se fosse código Python, retornando o resultado da expressão avaliada, como eval("2 + 2") que retorna 4'''

'''A função exec() em Python executa código Python dinamicamente, seja a partir de uma string ou de um objeto de código compilado, interpretando-o como um conjunto de instruções que são executadas no escopo atual, sem retornar um valor'''

'''A função help() em Python exibe a documentação (docstrings) de módulos, funções, classes e objetos diretamente no interpretador, permitindo entender como usar algo específico sem sair do ambiente de codificação'''

'''A função locals() em Python retorna um dicionário com todas as variáveis e símbolos presentes no escopo local atual (dentro de uma função, por exemplo), mostrando seus nomes como chaves e seus valores como itens'''

'''A função global() em Python é usada dentro de uma função para indicar que você quer trabalhar com uma variável que foi definida fora dela (no escopo global), permitindo que você a leia ou, mais importante, a modifique, alterando seu valor para todo o programa, em vez de criar uma nova variável local com o mesmo nome'''

