ordem = 1 
texto = input(f"Insira a palavra {ordem}: ")
concat = texto
while texto != "/exit":
    ordem += 1 
    texto = input(f"Insira a palavra {ordem}: ")
    if texto != "/exit":
        concat += " "+texto

print(concat)