nome_arquivo = input("Digite o nome do arquivo para armazenar as palavras: ")

with open(nome_arquivo, 'w') as arquivo: #quando o arquivo não existe, ele cria
    while True:
        palavra = input("Digite uma palavra ou /exit para encerrar: ")
        if palavra == "/exit":
            break
        arquivo.write(f"{palavra}\n")
#ao sair do if ele fecha o arquivo

print("Palavras armazenadas com sucesso...\n")

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteudo do arquivo:\n",conteudo)