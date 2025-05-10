#WAP to get the following output s='hai hello how are you' store as length in dictionary as a value 
'''a = input('Enter a string\n')
c = {}
for i in a.split():
    c[i]= len(i)
print(c)'''

#WAP to extract all the special character present inside given string, if length of output is >5, then print output as it is else print in reverse order

'''a = input('Enter a String\n')
b = ''

for i in a:
    if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
        b= b + i

if len(b)>5:
    print(b)
else:
    print(b[::-1])'''

#WAP to find sum of n natural numbers only if its even

'''n = int(input('Enter a number\n'))
sum = 0
if n%2==0:
    for i in range(1,n):
        sum += i
    print(sum)
else:
    print('number is odd number')'''

#WAP to print all the even number which are multiple of 5 and palindrome between the range

n = int(input('Enter a number\n'))

for i in range(1,n+1):
    if i%3==0 and i%2==0 and str(i)==str(i)[::-1]:
        print(i,'is a even and multiple of 3 & palindrome number')


# WAP to enter user name until it is correct

'''i = input('SET the USERNAME')
while True:
    a= input('Enter the correct user name\n')
    if a == i:
        print('Correct user name')
        break
    else:
        print('Enter again, incorrect username')'''
 


























