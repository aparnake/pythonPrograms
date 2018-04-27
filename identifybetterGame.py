import random

def rollDice():
    return (random.randrange(1,7))

Game1=rollDice()
print("Your Game1 number is: "+str(Game1))

Game2=rollDice()
print("Your Game2 number is: "+str(Game2))

Game2again=rollDice()
print("Your Game2again number is: "+str(Game2again))

if Game2>Game2again:
    Game2final=Game2
else:
    Game2final=Game2again

if Game1>Game2final:
    print("Game1 wins")
elif Game1<Game2final:
    print("Game2 wins")
else:
    print("Its a tie")




