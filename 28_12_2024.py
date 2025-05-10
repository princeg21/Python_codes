#WAP to reverse a number

'''num = int(input('enter a number\n'))
:qrev_num = 0
while num != 0:
    rev_num = 10*rev_num +(num%10)
    num = num//10

print('Reversed number:',rev_num)'''

#WAP to get the folloowing output>>s1=10011011101 & s2 = 11101100001 & output is 4

'''s1 = input('Enter a 0/1 string\n')
s2 = input('Enter a 0/1 string\n')

if len(s1)==len(s2):
    i =0
    count=0
    while i < len(s1):
        if s1[i]==s2[i]:
            count = count +1
        i = i+1
    print('output is:',count)
else:
    print('input string length is not same')'''

# WAP to count the number of occurance of specified character
'''a = input('ENTER a STRING\n')
b = input('ENTER a character\n')
i =0
count =0
while i < len(a):
    if a[i]== b:
        count = count +1
    i = i+1
print('Character',b,'occur',count,'times')

a = input('Enter a string')
b = input('Enter a character')
print(a.count(b))'''

#WAP to integers present in a list only if it is present at odd index

'''a = eval(input('Enter a List'))

i = 1
new_lst = []
while i <= len(a):
    if type(a[i]) == int:
        new_lst = new_lst + [a[i]]
    i = i+2

print('New List is:',new_lst)'''

#WAP to find the sum of cube of digits in a given string
'''a = input('Enter alphanumeric String\n')
i = 0
cube = 0
while i < len(a):
    if '0':<=a[i]<='9':
        cube = cube + (int(a[i])**3)
    i =i+1

print('Sum of cube is:',cube)''' #NOT DONE

#WAP to replace space by *, present in a string

'''a = input('Enter a String')
i=0
b = ''
while i<len(a):
    if a[i] == ' ':
        b = b + '*'
    else:
        b = b + a[i]
    i = i+1
print(b)'''



































