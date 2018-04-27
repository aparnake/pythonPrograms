import random

def rollDice():
    return (random.randrange(1,7))

def Game1():
    return rollDice()

def Game2():
    Roll1=rollDice()
    Roll2=rollDice()
    if Roll1>Roll2:
        return Roll1
    else:
        return Roll2    

Game1=Game1()
print("Your Game1 number is: "+str(Game1))

Game2final=Game2()
print("Your Game2 number is: "+str(Game2final))

if Game1>Game2final:
    print("Game1 wins")
elif Game1<Game2final:
    print("Game2 wins")
else:
    print("Its a tie")




