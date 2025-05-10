#WAP to check the number is prime number

'''n = int(input('Enter a number\n'))
for i in range(2,n):
    if n%i==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is a prime number')'''


#WAP to check that given list is homogenous or not

'''a = eval(input('Enter a List\n'))

for i in range(0,len(a)-1):
    if type(a[i]) != type(a[i+1]):
        print('List is non homogenous')
        break
else:
    print('List is homogenous')'''

#WAP to print the smallest factor of a given number except 1
n = int(input('Enter a number\n'))
for i in range(2,n):
    if n%i==0:
        print(i,'is smallest factor number for',n)
        break
else:
    print(n,'is smallest factor & prime number')




























