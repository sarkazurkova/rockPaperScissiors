import random


player = int(input("Type: 1 for ROCK, 2 for PAPER, 3 for SCISSORS").strip())
comp = random.randint(1, 3)
if comp == player:
    print("Draw!")
elif (comp == 1 and player == 2) or (comp == 2 and player == 3) or (comp == 3 and player == 1):
    print("You win!")
elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
    print(f"Computer chose {comp}")
    print("You loose")
else:
    print("Invalid enter...")