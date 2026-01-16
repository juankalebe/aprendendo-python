# utilizando bibliotecas e suas funções
import math # funções matemáticas
import os # funções para invocar funcionalidades do sistema operacional

x = 16
raiz_quad = math.sqrt (x)

print(f"Raiz quadrada de {x} é igual a {raiz_quad}")

angulo = 30
angulo_rad = math.radians(angulo) # convertendo de graus para radianos
seno = math.sin(angulo_rad) # essa função aqui espera o valor em radianos e não em graus
print(f"O seno de {angulo} graus é igual a {seno:.2f}")

diretorio = os.getcwd() # retorna o diretorio atual
print("Diretório corrente: ",diretorio)

os.system("ls") # ativa o terminal e escreve o comando que coloquei entre aspas