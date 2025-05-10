#WAP to print pattern
'''
r = int(input('Enter the number of rows\n'))

for i in range(r):
    for j in range(r):
        if i<=j:
            print(chr(ord('q')-r+j+1),end=' ')
        else:
            print(' ',end=' ')
    print() 
'''

#WAP to reverse the number without slicing
'''
a = int(input('Enter a number\n'))
rev = 0

while a!=0:
    n = a%10
    rev = (10*rev)+n
    a = a//10
print(rev)
'''

#WAP to check integer is single digit, double digit or triple digit
'''
n = int(input('Enter a number\n'))
count = 0

while n!=0:
    count=count+1
    n=n//10
print('No. of digit:',count)'''

#WAP to check the list
'''
a = eval(input('Enter  a list:\n'))

if len(a)%2==1:
    if type(a[len(a)//2])== str:
        print(a[len(a)//2][::-1])
    else:
        print('String is not present at middle')
else:
    print('Middle value not present')
'''

#WAP to print the pattern

r = int(input('Enter the number of rows\n'))
k=1
l=1
for i in range(r):
    for j in range(r):
        if i>=j:
            if i%2==0:
                print(l+2,end=' ')
                l = l+2
            else:
                print(k+1,end=' ')
                k= k+1
                l = k+2
        else:
            print(' ',end=' ')
    print()

