def maior (n1 , n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
     return n2
    else:
        return "são inguais"

numero1 = int(input("digite o primeiro numero:"))
numero2 = int(input("digite o primeiro numero:"))
            
print(maior(numero1 , numero2))