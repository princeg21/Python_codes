'''WAP to extract all the string datatypes from list using recursion'''
'''
def ex(l,nl=[],i=0):
    if len(l)<=i:
        return nl
    if type(l[i])==str:
        nl.append(l[i])
    return ex(l,nl,i+1)

print(ex(eval(input('List = \n'))))
'''
'''
def ex(l,nl=[]):
    if len(l)==0:
        return nl
    if type(l[0])==str:
        nl.append(l[0])
    l.pop(0)
    return ex(l,nl)

print(ex(eval(input('List = \n'))))
'''
#WAP to count no of uppercase alphabets present in a string
#WAP to count no of vowels present in a string 


class A:
    pass
print(type(A))
