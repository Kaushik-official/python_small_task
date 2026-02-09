
mylist=[3,7,2,9,4,1]
mylist.append(5)
print(mylist)

mylist=[3,7,2,9,4,1,2,5]
del mylist[2:3]
print(mylist)

mylist=[3,7,2,9,4,1,2,3,5]
mylist.sort()
print(mylist)

mylist=[3,7,2,9,4,1]
mylist.append(5)
del mylist[2:3]
mylist.sort()
mylist.sort(reverse=True)
print(mylist)

mylist=[3,7,2,9,4,1]
total=0
for i in mylist:
    total+=i
print(total)
    

mylist=[3,7,2,9,4,1]
print(len(mylist))
print(max(mylist))

