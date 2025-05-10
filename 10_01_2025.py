#WAP to get the following output input-> a = ['vishu',227,1,'last',22,18]; output-> b = [722,1,22,81]

'''a = eval(input('Enter a list\n'))
b = []

for i in a:
    if type(i)==int:
        n = i
        rev = 0
        while n!=0:
            rev = (rev*10) + n%10
            n = n//10
        b.append(rev)
print(b)

for i in a:
    if type(i)==int:
        rev = ''
        for j in str(i):
            rev = j + rev
        b.append(int(rev))
print(b)
'''

#WAP to print the pattern
'''r = int(input('Enter the no. of rows\n'))
c = int(input('Enter the no. of columns\n'))
for i in range(0,r):
    for j in range(0,c):
        print('*',end=' ')
    print()'''


'''r = int(input('Enter the no. of rows\n'))
for i in range(0,r):
    for j in range(0,r):
        if i==j:
            print(1,end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''r = int(input('Enter the no. of rows\n'))
for i in range(1,r+1):
    for j in range(0,i):
        print('*',end=' ')
    print()'''

'''r = int(input('Enter the no. of rows\n'))
for i in range(r):
    for j in range(r):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
r = int(input('Enter the no. of rows\n'))
for i in range(0,r):
    for j in range(0,(2*r)):
        if (r-i)==j or j==r+i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,r):
    for j in range(0,(2*r)-1):
        if i==j or j==(2*r)-1-i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
