#WAP to extract all the integer no present at odd index only if it is divisible by 5
'''
def ext():
    a = eval(input('Enter a list\n'))
    b = []
    for i in range(1,len(a),2):
        if type(a[i])==int:
            if a[i]%5==0:
               b.append(a[i])
    print(b)
ext()
'''

#WAP to string into dictionary with length as the value of each word
'''
def cal_dict():
    a = input('Enter a string\n')
    b = {}

    for i in a.split():
        b[i]= len(i)
    print(b)
cal_dict()
'''

#WAP to reverse each word of the string

def rev_word():
    a = input('Enter a string\n')
    b = ''

    for i in a.split():
        b= b + i[::-1] + ' '
    print(b)
rev_word()
