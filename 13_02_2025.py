n = int(input('Enter a number'))
x = ord('A')
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(x),end=' ')
            x = x+1
        print()
