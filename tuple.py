
t=(10,20,30)
x,y,z=t
print(x)
print(y)
print(z)


t=(10,20,30)
a,y,z=t
t=(z,y,a)
print(t)


t=(1,(2,3,4),5)
print(t[1])
print(t[1][1])


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
#a=a.union(b)
#a=a|b
#a=a.intersection(b)
#a=a&b
print(a-b)
print(a)


a = [1, 2, 2, 3, 4, 4, 5]
a=set([1, 2, 2, 3, 4, 4, 5])
a=list(a)
print(a)
