#WAP to find the sum of 2 int numbers using the 1st type of function
'''
def sum_2():
    a= int(input('Enter 1st value'))
    b= int(input('Enter 2nd value'))
    print(a+b)

sum_2()
'''

#WAP to find the multilication of 2 int numbers using the 1st type of function
'''
def multi_2():
    a= int(input('Enter 1st value'))
    b= int(input('Enter 2nd value'))
    print(a*b)

multi_2()
''' 

#WAP to find the length of the string
'''
def length():
    a = input('Enter a string\n')
    print(len(a))
length()
'''
#WAP to check the number of uppercase alphabets present in the string

def up_cal():
    a = input('Enter a string\n')
    count = 0
    for i in a:
        if 'A'<=i<='Z':
            count+=1
    print('Number of uppercase alphabets:',count)
up_cal()
