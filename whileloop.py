i=0
while i<10:
    if i%2==0:
        print("#########I is even")
    else:
        print("@@@@@@@@@I is odd")
    print("Papa loves mummy")
    print("Rams fav is mummy")
    print("Current value of i is:"+str(i))
    i=i+1
    print("Next value of i is:"+str(i))
    print("***********************************")

choice="Y"
while choice=="Y":
    print("I love you!")
    userChoice=input("Do you want more love:[Y/N]")
    if userChoice=="N":
        choice="N"
#    else userChoice=="Y":
#        choice=True

    
print("End of while loop")