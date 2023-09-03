Elabore um algoritmo que possa descobrir, através de perguntas e respostas, em qual área de um restaurante uma pessoa ou
grupo de pessoas precisa ser alocada.
O restaurante tem três áreas: térreo, 1ro andar, e área externa.
Clientes fumantes ou com animais de estimação precisam ser alocadas na área externa.
Grupos de 5 ou mais precisam ser alocados no 1º andar, pois não dá para juntar mesas no térreo.
Qualquer outro grupo de pessoas pode ser alocado no térreo. 


algoritmo

var
quantidadepessoa: inteiro
animal, fumante: caractere

inicio
escreva(“Olá, seja bem vindo ao Restaurante!”)
escreva(“São quantos pessoas?”)
leia(total_pessoa)
escreva(“Tem algum fumante?”)
leia(fumante)
escreva(“Tem animais?”)
leia(animal)

//se(fumante = fumante) ou (animal == animal) entao
   escreva(“Os cliente vai para aréa externa”)
    senao se(total_pessoa >= 5) entao
      escreva(“Os clientes irão para o 1° andar”)
      senao
        escreva(“Os clientes irão para o terreo”)
      fimse 
    fimse
fimse

fimse
