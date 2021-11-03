# Jogo_Sete_E_Meio
Trabalho da faculdade na qual tive que desenvolver um código em Python que simulasse o jogo de cartas Sete e Meio.



# Como funciona
  Joga-se sete e meio com as cartas do baralho, retirando-se do mesmo as cartas de valor igual a oito (8), 
nove (9) e dez (10). As figuras (valete, dama e rei) valem meio (0,5). O Ás vale 1,0 e as 
demais tem o valor que está escrito na carta. 
Após embaralhar as cartas é distribuída uma carta para o jogador e para a banca. Ambos 
olham a sua carta, sem mostrar ao outro e podem pedir mais uma carta, mais de uma vez. 
O objetivo é obter com a soma das cartas o valor sete e meio. Uma carta fica sempre oculta 
para o adversário, as outras, se existirem, são mostradas. Quando a banca e o jogador não 
quiserem mais cartas, aquelas escondidas são exibidas. 
Ganha a partida aquele que tiver o maior valor entre as cartas exibidas com limite máximo 
SETE E MEIO (7,5). Aquele cujo valor de suas cartas exceder sete e meio, perde. No caso de 
empate vence a banca.



# Caracteristicas do Código

Inicializei as cartas com a string (‘1234567JQK1234567JQK1234567JQK1234567JQK’) ou 
seja, no baralho existem 4 cartas de mesmo valor (o naipe não é relevante). 

Dentre as funções, existe uma que pega o baralho e embaralha ele. Isso através de um loop de 10 vezes, onde cada vez
é gerado um numero aleatorio n de 1 a 40, e a string (baralho) recebe em baralho[:n] + baralho [n:] só que este é invertido. Depois eu inverto a string como todo.


Este jogo é jogado entre a banca (computador) e um jogador (usuário).


# Exemplo de Saida

 Saida: Jogador1 – cartas: 7, J (sete e valete) = 7,5
 
 Jogador2 (banca) – cartas: 3, 7 (três e sete) = 10,0 excedeu o valor
 
 Jogador1 foi o vencedor
