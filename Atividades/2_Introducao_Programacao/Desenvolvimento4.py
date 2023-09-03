Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.



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
