def mySum(x,y,op):
    if op=='-':
        total= x - y
    elif op=='+':
        total= x + y
    return total

xx=20
yy=30
oper='-'
res=mySum(xx,yy,oper)
print("Result is :"+ str(res))