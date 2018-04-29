mylist=["dress","makeup","shoes","makeup"]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist.count("makeup"))
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

#treating list as a stack - LIFO
mylist.append("diamond")
print(mylist)
mylist.pop()
print(mylist[:2])
for i in mylist:
    print("forloop :"+i)


#2D list
my2dlist=[[1,2,3],[4,5,6],[7,8,"kkk"]]
print(my2dlist)


