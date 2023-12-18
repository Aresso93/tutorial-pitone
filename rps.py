import sys
import random

print('')
playerchoice = input("Inserisci... \n 1 per sasso \n 2 per carta \n 3 per forbice\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("Solo numeri da 1 a 3")

computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("Hai selezionato " + playerchoice + ".")
print("Python ha selezionato " + computerChoice + ".")
print("")

if player == 1 and computer == 3:
    print("Hai vinto!")
elif player == 2 and computer == 1:
    print("Hai vinto!")
elif player == 3 and computer == 2:
    print("🤑 Hai vinto!")
elif player == computer:
    print("Pareggioh")
else: 
    print("🍆 Hai perso!")