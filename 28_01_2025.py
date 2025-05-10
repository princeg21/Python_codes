#WAP to check that given number is prime
'''
def travel(n,l):
    for i in range(n,l):
        if isprime(i)==True:
            print(i,'is a prime number')

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

travel(int(input('Enter a number\n')),int(input('Enter a number\n')))
'''

#WAP to get output a='python' output-> b = 'ptoyhn' wih all 4 types
'''
def pat():
    a ='python'
    s =''
    k =''
    for i in range(len(a)):
        if i%2==0:
            s=s+a[i]
        else:
            k=k+a[i]
    print(s+k)
pat()
'''

#WAP to find the largest number in a list of integer with all the 4 types

'''
def max_num():
    l = eval(input('Enter a list\n'))
    max = l[0]
    for i in l:
        if i>max:
            max=i
    print(max,'is maximum number')
max_num()
'''
#WAP to convert number into binary
'''
def num_to_bin(n):
    b = ''
    while n!=0:
        b = str(n%2)+b
        n = n>>1
    return b
print(num_to_bin(int(input('Enter a number\n'))))
'''

#WAP to get the following output. input=>127342 & output => '242173' first even number then odd number

def extractor():
    n = int(input('Enter a number\n'))
    b = ''
    a = ''
    while n!=0:
        x = n%10
        if x%2==0:
            b = str(x)+b
        else:
            a = str(x)+a
        n=n//10
    print(b+a)
extractor()



























