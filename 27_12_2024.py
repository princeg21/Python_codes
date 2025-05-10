#WAP of print multiplication table

'''n = int(input('Enter a number\n'))

i =1
while i<=10:
    print(n,'X',i,'=',n*i)
    i = i+1'''

#WAP to find the product of n natural numbers

'''n = int(input('Enter a number\n'))

i = 1
mul = 1
while i<=n:
    mul = mul *i
    i = i+1
print(mul)'''

#WAP to get fibonacci series upto n terms

'''n = int(input('Enter the number\n'))
i = 0
i1 = 0
i2 = 1
next_num = i2
while i<n :
    print(next_num,end=' ')
    next_num = i1 + i2
    i1 = i2
    i2 = next_num
    i = i +1'''

# WAP to print all the characters of a string

'''string = input('Enter a string\n')

i = 0
while i< len(string):
    print(string[i])
    i =i+1
'''

#WAP to print all the characters present at even index

'''string = input('Enter a string\n')

i = 0
while i< len(string):
    print(string[i])
    i =i+2'''

# WAP to extract all the lower case characters present inside the string

'''a = input('Enter a string\n')
var = ''
i = 0
while i < len(a):
    if 'a'<= a[i]<='z':
        var = var + a[i]
    i = i +1
print(var)'''


'''a = input('Enter a string\n')
var = []
i = 0
while i < len(a):
    if 'a'<= a[i]<='z':
        var = var + list(a[i])
    i = i +1
b = str(var)#var is list data type and changing to string change all list into a string value
print(b)'''
