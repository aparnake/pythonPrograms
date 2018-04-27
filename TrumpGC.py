input1=input("Please enter your SSN: ")
criminalityStatus=input("Please enter if criminal: ")
input3=input("Please enter your credit score: ")
input4=input("Please enter your salary: ")
input5=input("Please enter your educational degree: ")

def criminalCheck(criminalityStatusInput):
    if criminalityStatusInput=="yes":
       criminalScore=(-2)
    elif criminalityStatusInput=="no":
        criminalScore=1
    return criminalScore

def creditCheck():
    if (input3>=0 and input3<=400):
        creditScore=0
    elif (input3>400 and input3<=800):
        creditScore=1
    return creditScore

def salary():
    if (input4>=0 and input4<=10000):
        salaryScore=0
    elif (input4>10000 and input4<=50000):
        salaryScore=1
    elif (input4>50000 and input4<=100000):
        salaryScore=2
    elif (input4>100000):
        salaryScore=3
    return salaryScore

def educationalDegree():
    if (input5=="no degree"):
        educationScore=0
    if (input5=="graduate"):
        educationScore=1
    if (input5=="post graduate"):
        educationScore=2
    if (input5=="phd"):
        educationScore=3
    return educationScore

Total1=criminalCheck(criminalityStatus)
Total2=creditCheck()
Total3=salary()
Total4=educationalDegree()

finalScore=(Total1+Total2+Total3+Total4)
print("Your final score is "+str(finalScore))
if (finalScore>=7):
    print("Congratulations! You will be issued a Green Card")
else:
    print("We are sorry! We cannot issue you a Green Card)")
        









 
        