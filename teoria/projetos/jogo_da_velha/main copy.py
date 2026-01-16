

matriz = [1,2,3,4,5,6,7,8,9] # matriz 3x3 do jogo da velha
velha = all(isinstance(item, str) for item in matriz) # retorna True se todos forem str
print (velha)

matriz = ["X","X","X","O","X","X",5,"X","X"] # matriz 3x3 do jogo da velha
velha = all(isinstance(item, str) for item in matriz) # retorna True se todos forem str
print (velha)