Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os identifiquem. 
Por exemplo, se o nome da equipe é “Os Lutadores”, o primeiro membro deve ter uma etiqueta “Os Lutadores – 1", o segundo 
membro “Os Lutadores – 2", e assim pela frente.

Elabore um algoritmo que permita ao usuário inserir o nome da equipe, e imprime etiquetas para os 5 membros da equipe seguindo
o exemplo mostrado acima.


Var
NomeEquipe: caractere;
Contador: Inteiro;


Inicio
Escreva(Qual o nome da sua equipe?: );
Leia(NomeEquipe):
Enquanto( Contador <= 5){
Escreva(Qual o nome da Equipe?: );
para contador = Contador <- 1 ate 5 faca;
Escreva(NomeEquipe,“-”,Contador);
fimpara
FimEnquanto;
