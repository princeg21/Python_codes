#WAP to find the factorial of a given number using recursion
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(int(input('n='))))
'''

#WAP to print sum of n natural number using recursion
'''
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(sum(int(input('n='))))
'''

#WAP to convert a number in reverse using recursion

def rev(n,out=0):
    a = n%10
    if n==0:
        return out
    out = (out*10)+a
    n = n//10
    return rev(n,out)
print(rev(int(input('n='))))


'''
def rev(n):
    a = n%10
    if n<10:
        return n
    n = n//10
    return int(str(a)+str(rev(n)))
print(rev(int(input('n='))))
'''
