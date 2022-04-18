import random
def rockPaperScissors(player):
    words = ["rock","paper","scissors"]
    cpu = random.choice(words)
    if(player == cpu):
        print("Draw")
        return 
    if(player == "rock" and cpu == "scissors"):
        print("Player Won!")
        return
    if(player == "paper" and cpu == "rock"):
        print("Player Won!")
        return
    if(player == "scissors" and cpu == "paper"):
        print("Player Won!")
        return
    else:
        print("You Loser! CPU WON!")
        return

while True:
    playerChoice = str(input())
    playerChoice.lower()
    rockPaperScissors(playerChoice)
