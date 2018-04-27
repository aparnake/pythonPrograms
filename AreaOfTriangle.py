#to calculate length of a line
def length(x1,y1,x2,y2):
    mylen=((((x2-x1)**2)+((y2-y1)**2))**0.5)
    return mylen
def areaOfTriangle(a,b,c):
    p=(a+b+c)/2
    area=((p*(p-a)*(p-b)*(p-c))**0.5)
    return area

# x1=input("Enter X1:")
# y1=input("Enter Y1:")
# x2=input("Enter X2:")
# y2=input("Enter Y2:")
# x3=input("Enter X3:")
# y3=input("Enter Y3:")
# print("Area of my triangle is: "+str(areaOfTriangle(length(x1,y1,x2,y2),length(x2,y2,x3,y3),length(x1,y1,x3,y3))))
