def interface():
    print(f"""  
               0   1   2
            0 [{tabuleiro[0][0]}] [{tabuleiro[0][1]}] [{tabuleiro[0][2]}]
            1 [{tabuleiro[1][0]}] [{tabuleiro[1][1]}] [{tabuleiro[1][2]}]
            2 [{tabuleiro[2][0]}] [{tabuleiro[2][1]}] [{tabuleiro[2][2]}]
          """)
    
def validarVitoria(rodada):
    global parar
    # Horizontal 0
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # Horizonal 1
    if(tabuleiro[1][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # Horizontal 2
    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
        
    # vertical 0
    if(tabuleiro[0][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # vertical 1
    if(tabuleiro[0][1] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][1] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # vertical 2
    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # diagonal 0
    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    # diagonal 2 
    if(tabuleiro[0][2] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][0] == rodada):
        interface()
        print(f"O {rodada} venceu!")
        parar = True
    
    

tabuleiro = [
             [" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]
            ]

parar = False
rodada = "X"
jogadas = 0


while parar == False:
    if jogadas == 9:
        interface()
        print("Empate!")
        parar = True

    interface()

    linha = int(input("Digite a linha escolhida: "))
    coluna = int(input("Digite a coluna escolhida: "))

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "O"

    elif rodada == "O":
        tabuleiro[linha][coluna] = "O"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "X"

# encerrar jogo!
print("Jogo Encerrado!") 