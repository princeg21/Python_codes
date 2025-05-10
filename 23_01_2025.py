#WAP to print following output: a = ['google.com','yahoo.com','py.pdf','amazon.in']
'''
def exte_ext():
    a = eval(input('Enter the list\n'))
    b = []
    for i in a:
        x = i.split('.')
        b.append(x[1])
    return b

print(exte_ext())
'''

def exte_ext():
    a = eval(input('Enter the list\n'))
    b = []
    for i in a:
        x = i.split('.')
        b.append(x[-1])
    return b

print(exte_ext())
