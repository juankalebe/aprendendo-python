'''
Crie um programa para simular uma calculadora. O programa deve ter quatro funções que sejam capazes de processar a soma, subtração, 
multiplicação e a divisão entre dois números. Crie um menu de opções para que o usuário possa escolher qual operação matemática deseja executar.
'''
menu = "Escolha o que deseja: \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\nO número de uma das opções de 1 a 5: "
verif = int(input(menu))

while verif <= 4 and verif >= 1:
    a = float(input("Insira o primeiro termo (a): "))
    b = float(input("Insira o segundo termo (b): "))

    match verif: # essa funcao só existe a partir da versão 3.10 do python. No lugar dela poderia usar if-elif-else em versões anteriores
        case 1:
            print(f"{a}+{b}={a+b:.2f}")
        case 2:
            print(f"{a}-{b}={a-b:.2f}")
        case 3:
            print(f"{a}x{b}={a*b:.2f}")
        case 4:
            print(f"{a}/{b}={a/b:.2f}")

    verif = int(input(menu))
