#WAP to print a pyramid shape and rombhus
'''
r = int(input('Enter the no. of rows'))

for i in range(r):
    for j in range(2*r-1):
        if r-1-i<=j<=r-1+i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(r-1):
    for j in range(2*r-2):
        if i+1<=j<=2*(r-1)-1-i :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#we can the range of i due to which shape of pyramid is reverse
for i in range(rr = int(input('Enter the no. of rows'))

for i in range(r):
    for j in range(2*r-1):
        if r-1-i==j or j==r-1+i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(r-1):
    for j in range(2*r-2):
        if i+1==j or j==2*(r-1)-1-i :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()-1,-1,-1):
    for j in range(2*r-1):
        if r-1-i<=j<=r-1+i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(r-1):
    for j in range(2*r-2):
        if i+1<=j<=2*(r-1)-1-i :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# alphabet triangle
'''
r = int(input('Enter the no. of character'))

for i in range(1,r+1):
    k = 0
    for j in range(1,r+1):
        if i+j<=r+1:
            if (r-i)%2==1:
                print(chr(ord('a')+k),end=' ')
            else:
                print(chr(ord('A')+k),end=' ')
            k=k+1
    print()
'''

# rombus without inside star
r = int(input('Enter the no. of rows'))

for i in range(r):
    for j in range(2*r-1):
        if r-1-i==j or j==r-1+i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(r-1):
    for j in range(2*r-2):
        if i+1==j or j==2*(r-1)-1-i :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
