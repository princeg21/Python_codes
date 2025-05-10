#WAP to check whether the number is perfect number or not

'''n = int(input('Enter a number'))
i = 1
sum = 0
while i<n:
    if n%i==0:
        sum = sum + i
    i = i+1

if sum == n:
    print(n,' is a perfect number')
else:
    print(n,' is not a perfect number')'''

#WAP to if the number is Armstrong number
n = int(input('Enter the number\n'))
n1 = n
n2 =n
l =0
while n1!=0:
    l =  l+1
    n1 = n1//10
i=0
sum=0
while n!=0:
    sum = sum + ((n%10)**l)
    n = n//10

if sum == n2:
    print(n2,'is a armstrong number')
else:
    print(n2, 'is not armstrong')


'''a = int(input('Enter a number'))
l = len(str(a))
out = 0
temp = a
while a!=0:
    ld = a%10
    out+=(ld**l)
    a = a//10
if out == temp:
    print(temp,'is armstrong number')
else:
    print(temp,'not a armstrong number')'''















