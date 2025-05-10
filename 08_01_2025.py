#WAP to guess the number

'''a = int(input('Enter a number\n'))
while True:
    b = int(input('Guess the number\n'))
    if a==b:
        print('Value matched')
        break
    elif a<b:
        print('it is greater, enter a smaller value')
    else:
        print('it is lesser value, enter a greater value')'''

'''import random
a = random.randint(1,10)

while True:
    b = int(input('Guess the number\n'))
    if a==b:
        print('Value matched')
        break
    elif a<b:
        print('it is greater, enter a smaller value')
    else:
        print('it is lesser value, enter a greater value')'''

#WAP to print all the even number in range 1 to 20

'''for i in range(1,21):
    if i%2==1:
        continue
    print(i)'''

#WAP to count no of different character in the string

'''a = input('Enter a string\n')
b= ''
for i in a:
    if i not in b:
        b= b+i
print(len(b))'''


#WAP to get the following output s = 'i love myself' out = {'i':1,'love':4,'myself':6}

'''a = input('Enter a string\n')
b =a.split()
c ={}
for i in b:
    count = 0
    for j in i:
        count= count+1
    c[i] = count

print(c)'''









































