*Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.
*
Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg. 


def categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas):
    if quantidade_rodas == 2 or quantidade_rodas == 3:
        return "Categoria A"
    elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
        return "Categoria B"
    elif quantidade_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
        return "Categoria C"
    elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
        return "Categoria D"
    elif quantidade_rodas >= 4 and peso_bruto > 6000:
        return "Categoria E"
    else:
        return "Categoria não identificada"

# Entrada de dados
quantidade_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso bruto do veículo em quilogramas: "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

# Determinar a categoria de habilitação
categoria = categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas)

# Exibir a categoria de habilitação necessária
print("A categoria de habilitação necessária para o veículo informado é:", categoria)
