#WAP to convert binary into numbers
'''
def bin_to_num():
    bi = input('Enter a binary string\n')
    num = 0
    for i in range(len(bi)):
        if bi[i]=='1':
            num = num + 2**(len(bi)-1-i)
    print(num)
bin_to_num()
'''

#WAP to find the 2nd maximum value from the list

def max_2():
    l =eval(input('Enter a list\n'))
    max1 = l[0]
    max2 = float('-inf')
    for i in l:
        if i>max1:
            max1 = i
    for i in l:
        if i>max2 and max1>i:
            max2 = i
    print(max2)
max_2()


#WAP for following input s='aaabbbcccdf' output->a3b3c3d1f1
'''
s = input('Enter a string\n')
b = ''
for i in range(len(s)):
    if s[i] not in b:
        count =1
        b=b+s[i]
    elif s[i]==s[i-1]:
        count+=1
    elif s[i]!=s[i+1]:
        b+= str(count)
print(b)
'''
