# jogo da velha começa com uma matriz 3x3
# o jogo acaba quando uma das linhas está completa: horizontal ou diagonal
# são dois jogadores fazendo isso alternadamente 
# até um deles conseguir completar uma linha ou dar velha: quando todos os espaços são preenchidos e a combinação de 3 não é alcançada
import os
def visualizar_jogo (lista):
    print()
    for i in range(9):
        if (i+1) == 1 or (i+1) == 4 or (i+1) == 7: 
            print("|",end="   ")
        print(lista[i],end="   ")
        if (i+1)%3==0:
            print("|")
    print()

matriz = [1,2,3,4,5,6,7,8,9] # matriz 3x3 do jogo da velha

velha = False

while not(velha):
    os.system('clear')
    print("JOGADOR 1: X\tJOGADOR 2: O")
    visualizar_jogo(matriz)

    verif = True
    while verif:
        pos_jog1 =int(input("Jogador 1, escolha a posição da sua jogada: "))
        if pos_jog1 >= 1 and pos_jog1 <= 9:
            verif = False
            matriz[pos_jog1-1] = "X"
        visualizar_jogo(matriz)
    
    verif = True
    while verif:
        pos_jog2 =int(input("Jogador 2, escolha a posição da sua jogada: "))
        if pos_jog2 >= 1 and pos_jog2 <= 9:
            verif = False
            matriz[pos_jog2-1] = "O"

    # verificar se alguma linha foi completa ou se todos os espaços da matriz foram preenchidos (velha)
    # possiveis: 123, 147, 159, 258, 369, 357, 456, 789

    if (matriz[0] == matriz[1] and matriz[1] == matriz[2]): # 123
        break
    elif (matriz[0] == matriz[3] and matriz[3] == matriz[6]): #147
        break
    elif (matriz[0] == matriz[4] and matriz[4] == matriz[8]): #159
        break
    elif (matriz[1] == matriz[4] and matriz[4] == matriz[7]):#258
        break
    elif (matriz[2] == matriz[5] and matriz[5] == matriz[8]):#369
        break
    elif (matriz[2] == matriz[4] and matriz[4] == matriz[6]):#357
        break
    elif (matriz[3] == matriz[4] and matriz[4] == matriz[5]):#456
        break
    elif (matriz[6] == matriz[7] and matriz[7] == matriz[8]):#789
        break
    else:
        velha = all(isinstance(item, str) for item in matriz) # retorna True se todos forem str
    


