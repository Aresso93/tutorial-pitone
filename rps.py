import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))

print('')
playerchoice = input("Inserisci... \n 1 per sasso \n 2 per carta \n 3 per forbice\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("Solo numeri da 1 a 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("Hai selezionato " + str(RPS(player)).replace('RPS.','') + ".")
print("Python ha selezionato " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player == 1 and computer == 3:
    print("🤑 Hai vinto!")
elif player == 2 and computer == 1:
    print("🤑 Hai vinto!")
elif player == 3 and computer == 2:
    print("🤑 Hai vinto!")
elif player == computer:
    print("👔 Pareggioh")
else: 
    print("🍆 Hai perso!")