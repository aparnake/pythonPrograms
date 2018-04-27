import random
userChoice1=input("Please enter your choice")
if (userChoice1=="rock" or userChoice1=="scissors" or userChoice1=="paper"):
    print("User picked "+userChoice1)
else: 
    print("not a valid choice")
    quit()
computerChoice=random.choice(['rock','scissors','paper'])
print("Computer picked "+computerChoice)

if (userChoice1=="rock" and computerChoice=="scissors"):
    print("You win!")
if (userChoice1=="scissors" and computerChoice=="rock"):
    print("You lose!")
if (userChoice1=="paper" and computerChoice=="rock"):
    print("You win!")
if (userChoice1=="rock" and computerChoice=="paper"):
    print("You lose!")
if (userChoice1=="scissors" and computerChoice=="paper"):
    print("You win!")
if (userChoice1=="paper" and computerChoice=="scissors"):  
    print("You lose!")
if (userChoice1=="paper" and computerChoice=="paper"):  
    print("Nobody wins or loses")
if (userChoice1=="scissors" and computerChoice=="scissors"):  
    print("Nobody wins or loses")
if (userChoice1=="rock" and computerChoice=="rock"):  
    print("Nobody wins or loses")
