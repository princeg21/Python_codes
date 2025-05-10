#WAP to get the following output input->'apple is good'; output ->{'apple':2,'is':1,'good':2}
'''
def word_spliter(s):
    a = {} 
    for i in s.split():
        a[i]=vowel_counter(i)
    return a

def vowel_counter(s):
    count = 0
    for j in s:
        if j in 'aeiouAEIOU':
            count=count+1
    return count

print(word_spliter(input('Enter a string\n')))
''' 

# WAP to extract all the palindrome string present in a list without using slicing
'''

def is_palindrome(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            break
    else:
        return s

def list_traverse(l):
    a = []
    for i in l:
        a.append(is_palindrome(i))
    return a

print(list_traverse(eval(input('Enter a list\n'))))
'''
#solution 2
'''
def palindrome(i):
    b=''
    for j in i:
        b =j+b
    if i==b:
        return True
    else:
        return False
def main(l):
    out=[]
    for i in l:
        if type(i)==str:
            if palindrome(i)==True:
                out.append(i)
    return out

print(main(eval(input('Enter the list\n'))))
'''
'''
def is_palindrome(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
            break
    else:
        return True

def list_traverse(l):
    a = []
    for i in l:
        if type(i)==str:
            if is_palindrome(i):
                a.append(i)
    return a

print(list_traverse(eval(input('Enter a list\n'))))
'''
#WAP to check that given number is strong no -> factorial of all the digit of the number is equal to number

'''
def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial
def sum_digit(n):
    sum=0
    while n%10!=0:
        sum += fact(n%10)
        n = n//10
    return sum
a =int(input('Enter a number\n'))
if sum_digit(a)==a:
    print(a,'is strong number')
else:
    print(a,'not strong number')
'''



























