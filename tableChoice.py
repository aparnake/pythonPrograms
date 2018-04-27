def printTable(mytableNumber):
    i=1
    while i<11:
        print(str(mytableNumber)+" * "+str(i) + " = "+str(mytableNumber*i))
        i=i+1
        
choice='Y'    
while choice=='Y':
    tableof=input("Please enter the table number: ")
    printTable(tableof)
    choice=input("Do you want to continue [Y/N]: ")

    