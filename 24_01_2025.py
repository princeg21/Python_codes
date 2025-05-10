#WAP to add 3 numbers
'''
def sum(a,b,c):
    return a+b+c
print(sum(int(input()),int(input()),int(input())))
'''

#WAP to perform a calculator function
'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def inp():
    a = int(input('Enter 1st number\n'))
    b = int(input('Enter 2nd number\n'))
    return a,b

print('Enter the choice\n 1. addition\n 2. subtraction\n 3. multiplication\n 4. division\n 5. To stop program')

while True:
    choice = int(input('Enter your choice\n'))
    if choice == 1:
        x,y = inp()
        print(add(x,y))
    elif choice == 2:
        x,y = inp()
        print(sub(x,y))
    elif choice == 3:
        x,y = inp()
        print(mul(x,y))
    elif choice == 4:
        x,y = inp()
        print(div(x,y))
    else:
        print('Thanks for your time')
        break
'''
