def mult_de2 (A, B): # variaveis no escopo local apenas
    return A * B

def div_de2 (A, B): # variaveis no escopo local apenas
    if B == 0:
        print("Divisor igual a zero")
    else:
        return A / B