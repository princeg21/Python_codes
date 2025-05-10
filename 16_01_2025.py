#WAP with alphabet and numbers

r = int(input('Enter the no. of rows'))

for i in range(r):
    k,l =0,1
    for j in range(2*r):
        if r-1-i<=j<=r-1:
            print(l,end=' ')
            l = l+1
        elif r<=j<=r+i:
            print(chr(ord('a')+k),end=' ')
            k = k+1
        else:
            print(' ',end=' ')
    print()
for i in range(r):
    k=0
    for j in range(2*r):
        if i<=j<=r-1:
            print(j+1,end=' ')
        elif r<=j<=(2*r)-i-1:
            print(chr(ord('A')+k+i),end=' ')
            k=k+1
        else:
            print(' ',end=' ')
    print()

#WAP to build a rombous
'''
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
'''
