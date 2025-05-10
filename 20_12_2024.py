#WAP to find the greatest of three number
'''num1 = int(input('Enter number 1\n'))
num2 = int(input('Enter number 2\n'))
num3 = int(input('enter nnumber 3\n'))
if num1 > num2 and num1 >num3:
    print('number 1 is greatest')
elif num2 > num1 and num2>num3:
    print('number 2 is greatest')
else:
    print('number 3 is greatest')'''

#WAP to check relation between 2 integer input
'''num1 = int(input('Enter number 1\n'))
num2 = int(input('Enter number 2\n'))
if num1 > num2:
    print(num1,'is greater than',num2)
elif num2 > num1:
    print(num1,'is less than',num2)
else:
    print(num1,'equal to', num2)'''

#WAP to login into instagram with valid username and password
'''username = input('Enter your username\n')
valid_username = 'princeg21'
valid_password = 'admin'
if username == valid_username:
    password = input('Enter the password\n')
    if password == valid_password:
        print('login successful')
    else:
        print('incorrect password')
else:
    print('username is incorrect')'''

# WAP to print middle value of a list onlly if it is string
'''val = eval(input('Enter a list\n'))
if len(val)%2==1:
    if type(val[len(val)//2])== str:
        print(val[len(val)//2])
    else:
        print('not a string datatype')
else:
    print('not a middle value list')'''

#WAP to check the character is vowel or not

char = input('enter a character value\n')

if 'a'<=char<='z' or 'A'<=char<='Z':
    if char in 'aeiouAEIOU':
        print(char,'is vowel')
    else:
        print(char,'is consonant')
else:
    print('It is not a alphabet')























