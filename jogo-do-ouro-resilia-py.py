def linha ():
    print ("="*60)

def espaco ():
    print (" ")


titulo = "Bem vindos ao jogo do ouro!"

linha ()
print ("Bem vindos ao jogo do ouro!".center(60))
linha ()

nome = input("Qual o seu nome? ")
idade = int(input("Quantos anos você tem? "))


if idade <= 9:
    print("O jogo só é permitido para maiores de 10 anos!")
elif idade >= 10:
    print ("CLASSIFICAÇÃO: +10")
    print ("GÊNERO: Mistério / Investigação")
    linha ()

    print (" ... Numa cidade chamada Ouro Preto no Interior de Minas, aconteceu uma festa\n\
    em que toda a cidade estava presente.\n\
    Nesta festa todos beberam um suco verde que é tradição da cidade.")

    linha ()
    print ("Diante deste ocorrido, analise três situações ocorridas nesta festa:")
    espaco()
    print ("A. Pessoas diferentes começaram a ter sonhos com uma árvore. Na primeira noite, \n\
    Luiza sonhou com uma árvore que dava frutos o ano inteiro verde e no sonho tinha um senhor, \n\
    vestido de branco, disse a ela que o sonho dela estava na árvore da cidade. E assim o sonho acabou!")
    espaco()

    print("B. Na mesma semana Claudio sonhou retirando de uma árvore no centro da cidade \n\
    uma caixa e nela tinham maçãs verdes. E assim, o sonho dele acabou!")
    espaco()

    print("C. A última pessoa, que foi a Laura, sonhou comendo uma maçã verde \n\
    em frente a igreja da cidade e a maçã que se mostrava verde por fora era uma barra de ouro por dentro. \n\
    E assim acabou o sonho desta terceira pessoa!")
    espaco()

    print("Diante destes três cenários. Você será o investigador. A história possui três elementos com ligações! Tente descobrir!!")
    espaco()


    pergunta_de_abertura = int(input(" Escolha: O que você faz neste momento? 1. Procura pistas nos SÍTIOS da cidade? \n\
    2. Procura pistas nas IGREJAS?  3.Procura pistas no CENTRO da cidade? "))
    if pergunta_de_abertura == 1:
        primeira_camada_primeiro_cenario = int(input("Escolha: 1. Perguntar a índios da região? \n\ 2. Perguntar a moradores? "))
        if primeira_camada_primeiro_cenario == 1:
            print("Você descobre que os índios foram explorados na Mina da região e sentem-se \n\
            revoltados com as histórias sobre a cidade! Você deveria ter feito a ligação dos elementos principais:\n\
            A maçã verde, a árvore e a igreja!")
            espaco()
            print(" === FIM de JOGO! VOCÊ PERDEU! === ")
            print("Pense melhor e tente novamente!!")
        elif primeira_camada_primeiro_cenario == 2:
            print("Moradores te aconselham a contar todas as maçãs que encontrar!")
            espaco()
            print("Você percebe que prejudicou a natureza! Você deveria ter feito a ligação dos elementos principais:\n\
            A maçã verde, a árvore e a igreja!")
            print(" === FIM de JOGO! VOCÊ PERDEU! === ")
            print("Pense melhor e tente novamente!!")
        else:
            print("Erro! Digite a opção 1 ou 2!!")
    elif pergunta_de_abertura == 2:
        primeira_camada_segundo_cenario = int(input(" Escolha: 1. Conversa com o padre? \n\
        2. Conversa com pessoas dentro da igreja para entender as histórias da cidade? "))
        if primeira_camada_segundo_cenario == 1:
            segunda_camada_segundo_cenario = int(input("Escolha: 1.Perguntar ao padre relação do ouro com algo que já foi enterrado? \n\
            2. Perguntar ao padre sobre histórias das árvores ao redor da igreja?"))
            if segunda_camada_segundo_cenario == 1:
                print ("O padre conta sobre os costumes antigos da igreja, revelando sobre os corpos.  \n\
                Você encontra as ossadas dos bispos e com elas, muito ouro!")
                print (" === VOCÊ VENCEU!!! PARABÉNS!! === ")
            elif segunda_camada_segundo_cenario == 2:
                print ("O padre faz uma relação do ouro com as colunas da igreja e isso não te leva a lugar nenhum! Você deveria ter feito \n\
                a ligação dos elementos principais:\n\
                A maçã verde, a árvore e a igreja!")
                print (" === FIM de JOGO! VOCÊ PERDEU! === ")
                print ("Pense melhor e tente novamente!!")
            else:
                print ("Erro! Digite a opção 1 ou 2!!")
        elif primeira_camada_segundo_cenario == 2:
            print ("Os moradores não conhecem bem a história da cidade! Você deveria ter feito a ligação dos elementos principais:\n\
            A maçã verde, a árvore e a igreja!")
            print (" === FIM de JOGO! VOCÊ PERDEU! === ")
            print ("Pense melhor e tente novamente!!")
        else: 
            print ("Erro! Digite a opção 1 ou 2!!")
    elif pergunta_de_abertura == 3:
        primeira_camada_terceiro_cenario = int(input(" Escolha: 1. Pesquisar com moradores sobre butijas (Baús) de ouro? \n\ 2. Perguntar a moradores sobre histórias do ouro? "))
        if primeira_camada_terceiro_cenario == 1:
            segunda_camada_terceiro_cenario = int(input("Escolha: 1. Acreditar que seja apenas lendas urbanas? \n\
            2. Acreditar que não existem mais butijas na cidade, mas que antigos morriam e enterravam entes queridos com pertences?"))
            if segunda_camada_terceiro_cenario == 1:
                print("Você deveria ter feito a ligação dos elementos principais:\n\
                A maçã verde, a árvore e a igreja!")
                print (" === FIM de JOGO! VOCÊ PERDEU! === ")
                print ("Pense melhor e tente novamente!!")
            elif segunda_camada_terceiro_cenario == 2:
                    terceira_camada_terceiro_cenario = int(input(" Escolha: Você faz uma ligação do que escutou na igreja  \n\
                    com algo que possa estar enterrado na frente da igreja? 1. Sim!   2. Não!"))
                    if terceira_camada_terceiro_cenario == 1:
                        print("Você encontra ossadas de bispos e com elas muito ouro!")
                        print (" === VOCÊ VENCEU!!! PARABÉNS!! === ")
                    elif terceira_camada_terceiro_cenario == 2:
                        print("Você deveria ter feito a ligação dos elementos principais:\n\
                        A maçã verde, a árvore e a igreja!")
                        print (" === FIM de JOGO! VOCÊ PERDEU! === ")
                        print ("Pense melhor e tente novamente!!")
                    else:
                        print ("Erro! Digite a opção 1 ou 2!!")
            else:
                print ("Erro! Digite a opção 1 ou 2!!")
        elif primeira_camada_terceiro_cenario == 2:
            segunda_camada_terceiro_cenario_segunda_opcao = int(input("Após histórias de Minas de ouro existentes na cidade.  \n\
            Você continua investigação? 1. Sim!  2. Não!"))
            if segunda_camada_terceiro_cenario_segunda_opcao == 1:
                print("Você descobre que exploração ilegal de ouro não existe mais! Você deveria ter feito a ligação dos elementos principais:\n\
                A maçã verde, a árvore e a igreja!")
                print (" === FIM de JOGO! VOCÊ PERDEU! === ")
                print ("Pense melhor e tente novamente!!")
            elif segunda_camada_terceiro_cenario_segunda_opcao == 2:
                print("Você deveria ter feito a ligação dos elementos principais:\n\
                A maçã verde, a árvore e a igreja!")
                print (" === FIM de JOGO! VOCÊ PERDEU! === ")
                print ("Pense melhor e tente novamente!!")
            else:
                print ("Erro! Digite a opção 1 ou 2!!")
        else:
            print ("Erro! Digite a opção 1 ou 2!!")
    else:
        print ("Erro! Digite a opção 1 ou 2 ou 3!!")
else:
    print ("Erro de digitação!!")


