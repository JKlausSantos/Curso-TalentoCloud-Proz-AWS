Elabore um algoritmo para que o usuário, através da entrada de dados, informe os seus dados pessoais. Alguns desses dados
fornecidos pelo usuário precisam ser apresentados na tela quando o algoritmo for executado, são eles:
- Nome;
- Endereço;
- Cidade;
- CPF;
- RG.


Var
nome:caractere
endereco:caractere
cidade:caractere
cpf:inteiro
rg:inteiro

Inicio
escreva ("Digite seu nome: ")
leia (nome)
escreva ("Digite seu endereço: ")
leia (endereco)
escreva ("Digite sua Cidade: ")
leia (cidade)
escreva ("Digite o número de seu CPF [sem pontos ou traços]: ")
leia (cpf)
escreva ("Digite o número de seu RG [sem pontos ou traços]: ")
leia (rg)

escreva ("NOME: ", nome,".")
escreva ("ENDERECO: ", endereco," - ", cidade)
escreva ("CPF: ", cpf)
escreva ("RG: ", rg)

FimAlgoritmo

