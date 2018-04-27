userChoice1=input("Please enter number 1 ")
userChoice2=input("Please enter number 2 ")
userChoice3=input("Please enter sign ")
def operator():
    if (userChoice3=="+"):
        Answer=(userChoice1+userChoice2)
        print("Your answer is "+str(Answer))
    elif (userChoice3=="-"):
        Answer=(userChoice1-userChoice2)
        print("Your answer is "+str(Answer))
    elif (userChoice3=="*"):
        Answer=(userChoice1*userChoice2)
        print("Your answer is "+str(Answer))
    elif (userChoice3=="/"):
        Answer=(userChoice1/userChoice2)
        print("Your answer is "+str(Answer))
Final=operator()




