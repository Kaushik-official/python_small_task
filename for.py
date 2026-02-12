
for i in range(1,21):
    print(i)

n=int(input())
for i in range(1,n+1):
    print(i)

for i in range(0,21,2):
    print(i)

n=int(input())
for i in range(0,n+1,2):
    print(i)

n=int(input())
a=0
for i in range(1,n+1):
    print(i)
    a=i+a
print(a)

n=int(input())
a=0
for i in range(1,n+1):
    a=i+a
print(a)

n=int(input())
for i in range(11):
    print(n,"*",i,"=",n*i)


text = input("Enter a string: ")
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)