#For LOOP

'''s = [336,54,557,4646,234]
for i in s:
    print(i,type(i))'''



'''a = [1,12,3+4j,56.78,True]
for i in a:
    if type(i) == int:
        print(i)'''

#WAP to extract all the string present at even index in a list

a = eval(input('Enter a list of different data types\n'))
b = []

for i in range(0,len(a),2):
    if type(a[i])==str:
        b = b + [a[i]]

print(b)



