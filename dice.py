import random

def rollDice3Times():
    return (random.randrange(1,7))+(random.randrange(1,7))+(random.randrange(1,7))

Totaluser=rollDice3Times()
print("Your total is: "+str(Totaluser))
Totalcomputer=rollDice3Times()
print("Computer Totalis: "+str(Totalcomputer))
if (Totaluser>Totalcomputer):
    print("You win!")
elif(Totaluser==Totalcomputer):
    print("its a tie")
else:
    print("You lose!")
    

