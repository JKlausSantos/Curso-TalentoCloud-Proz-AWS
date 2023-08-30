def calculadora(numero1, operador, numero2):
    if operador == "+" : return numero1 + numero2

    elif operador == "-": return numero1 - numero2

    elif operador == "*": return numero1 * numero2

    elif operador == "/": return numero1 / numero2

    else : return 0

numero1=int(input("Digite um número: "))

operador=str(input("Digite um operador: "))

numero2=int(input("Digite um número: "))

resultado=(calculadora(numero1, operador, numero2))
print(resultado)