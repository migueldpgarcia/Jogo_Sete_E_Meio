#Autor: Miguel de Pino Garcia


import random

#
#Funções
#

def embaralha(string):
    i = 1
    while i <= 10:
        numero = random.randint(1,len(string))
        string = string[:numero] + inverteString(string[numero:])
        #Percebi que da forma do anunciado, raramente a string[0] ou string[1] era alterado, logo sempre invertirei a string a cada passo do loop
        string = inverteString(string)
        i += 1
    return string


def inverteString(string):
    string_nova = string[-1::-1]
    return string_nova


def Pontuacao(string):
    count_teste= 0
    soma = 0
    while count_teste < len(string):
        if string[count_teste] in 'JQK':
            soma += 0.5
        else:
            soma += float(string[count_teste])
        count_teste += 1
    return soma

def BaralhoEspacado(string):
    nova_string = ''
    for i in range (0,len(string)):
        nova_string += string[i] + ' '
    return nova_string


def CondicaoPontuacao(pontuacao):
    if pontuacao > 7.5:
        return 'excedeu o valor'
    return ''


def POR_ESCRITO(string):
    string_nova = ''
    i = 0
    while i < len(string):
        if i > 0:
            string_nova += 'e '
        if string[i] == '1':
            string_nova += 'um'
        elif string[i] == '2':
            string_nova += 'dois'
        elif string[i] == '3':
            string_nova += 'tres'
        elif string[i] == '4':
            string_nova += 'quatro'
        elif string[i] == '5':
            string_nova += 'cinco'
        elif string[i] == '6':
            string_nova += 'seis'
        elif string[i] == '7':
            string_nova += 'sete'
        elif string[i] == 'J':
            string_nova += 'valete'
        elif string[i] == 'Q':
            string_nova += 'dama'
        elif string[i] == 'K':
            string_nova += 'rei'
        if i < len(string) - 1:
            string_nova += ' ' #Porque só a ultima palavra não terá o espaço, conforme a saida do anunciado
        i += 1
    return string_nova
    

#
#Bloco Principal
#
def main():
    baralho = '1234567JQK1234567JQK1234567JQK1234567JQK'

    baralho = embaralha(baralho)

    Jogador1 = ''

    Jogador2 = ''

    Jogador1_Continuar = True

    Jogador2_Continuar = True

    print('Seja bem vindo ao jogo sete e meio, onde o objetivo é que suas cartas somem 7 e meio (J,Q,K valem 0,5)')
    while Jogador1_Continuar == True or Jogador2_Continuar == True:
        if Jogador1_Continuar:
            baralho = baralho[1:]
            Jogador1 = Jogador1 + baralho[0]
        print('Suas cartas são: %s'%BaralhoEspacado(Jogador1))
        if Jogador2_Continuar:
            baralho = baralho[1:]   
            Jogador2 = Jogador2 + baralho[1]
        print('As cartas VISÍVEIS do adversário são: %s'%BaralhoEspacado(Jogador2[1:]))
        Jogador1_Continuar = bool(input('Você quer mais uma carta para esta rodada? (Enter para não, qualquer letra para sim): '))
        if Pontuacao(Jogador2) >= 6: #Poderia ser outros valores aqui, a ideia é que se ele chegou ou passou de 6.5, provavelmente a banca vai passar do limite na prox rodada
            Jogador2_Continuar = False
        if Jogador2_Continuar and not(Jogador1_Continuar):
            print('Jogador 2(banca) comprou uma carta, logo teremos mais uma rodada!')

    # Casos
    print("Jogador1 – cartas: %s(%s)= %.2f %s" %(BaralhoEspacado(Jogador1),POR_ESCRITO(Jogador1),Pontuacao(Jogador1), CondicaoPontuacao(Pontuacao(Jogador1))))
    print("Jogador2(banca) – cartas: %s(%s)= %.2f %s" %(BaralhoEspacado(Jogador2),POR_ESCRITO(Jogador2),Pontuacao(Jogador2), CondicaoPontuacao(Pontuacao(Jogador2))))


    if Pontuacao(Jogador1) > 7.5 and Pontuacao(Jogador2) > 7.5:
        print("Ambos passaram do limite, logo O jogador 2 venceu")
    elif Pontuacao(Jogador1) <= 7.5 and Pontuacao(Jogador2) > 7.5:
        print("O jogador 1 venceu")
    elif Pontuacao(Jogador2) <= 7.5 and Pontuacao(Jogador1) > 7.5:
        print("O jogador 2 venceu")
    elif Pontuacao(Jogador1) >  Pontuacao(Jogador2):
        print("O jogador 1 venceu")
    elif Pontuacao(Jogador2) > Pontuacao(Jogador1):
        print("O jogador 2 venceu")
    else:
        print("Empate na pontuação, logo o jogador 2 venceu")
main()






