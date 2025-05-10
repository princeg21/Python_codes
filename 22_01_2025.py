#WAP a program to revrse the string
'''
def rev(s):
    print(s[::-1])

rev(input('Enter a string\n'))
'''

#WAP to get the following output-> 'how are you' => 'you are you'
'''
def rev_str(s):
    a = s.split()[::-1]
    print(' '.join(a))

rev_str(input('Enter a string\n'))
'''

#WAP to get the following output -> a=10011, b=00101 & output is 2
'''
def sim_check(a,b):
    count = 0
    for i in range(len(a)):
        if a[i]==b[i]:
            count =count+1
    print(count)

sim_check(input('Enter a binary data'),input('Enter b binary data'))
'''

def check(a,b):
    cn =0
    for i,j in zip(a,b):
        if i==j:
            cn+=1
    print(cn)

check(input('Enter a binary data\n'),input('Enter b binary data\n'))
