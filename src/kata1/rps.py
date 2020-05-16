from random import randint

def quienGana(player, ai):
    
    if player == ai :      
        return 'Empate!' 
    elif (player== 'Tijeras' and ai =='Papel') or (player== 'Piedra' and ai== 'Tijeras') or (player == 'Papel' and ai == 'Piedra'):
        return 'Ganaste!'   
    else:
        return 'Perdiste!'
  
  
def Game():

    mi_entrada = 'input("Escribe Piedra papel o tijeras")'
    player = mi_entrada.lower().capitalize()
    options = ["Piedra", "Papel", "Tijeras"]
    ai = options[randint(0,2)]
    ai=ai.lower().capitalize()
    print(player)
    print(ai )
    winner = quienGana(player, ai)
    print(winner)
    
Game()

