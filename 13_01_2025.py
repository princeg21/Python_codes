#WAP
'''r = int(input('Enter the no. of rows\n'))
b= (2*r)-1
for i in range(1,r+1):
    for j in range(1,b+1):
        if i+j==r+1 or j-i==r-1 or i==r:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''r = int(input('Enter the no. of rows\n'))
for i in range(0,r):
    for j in range(1,(2*r)): 
        if (r-i)==j or j==r+i or i==r-1:
            print('*',end=' ') 
        else: 
            print(' ',end=' ') 
    print()
'''

r = int(input('Enter the number of rows\n'))

for i in range(1,r+1):
    k =1
    for j in range(1,r+1):
        if i>=j:
            if i%2==0:
                print(k**2,end=' ')
            else:
                print(k,end=' ')
            k = k+1
    print()

