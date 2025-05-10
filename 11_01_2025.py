#WAP to build a pattern to find secondary diagonal

'''a = int(input('Enter Diagonal length'))
for i in range(a):
    for j in range(a):
        if j == a-i-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''a = int(input('Enter Triangle length'))
for i in range(a):
    for j in range(a):
        if j >= a-i-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


a = int(input('Enter Triangle length'))
for i in range(a):
    for j in range(a):
        if j+i <= a-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''a = int(input('Enter number of rows'))
for i in range(1,a+1):
    for j in range(1,i+1):
            print(j,end=' ')
    print()'''

'''a = int(input('Enter the number of rows'))

for i in range(a):
    k = i+1
    for j in range(k):
        print(k,end=' ')
        k=k+1
print()'''


a = int(input('Enter the number of rows'))

for i in range(a):
    k = i+1
    for j in range(a):
        if i>=j:
            print(k,end=' ')
            k=k+1
        else:
            print(' ',end=' ')
    print()
