- Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
- A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
no ano atual (2022).
- Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja preenchido.


import datetime

def obter_ano_de_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def main():
    nome_completo = input("Digite o nome completo: ")
    ano_nascimento = obter_ano_de_nascimento()
    idade = calcular_idade(ano_nascimento)

    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __nome__ == "__main__":
    main()
