#WAP to extract all the uppercase characters present in a string only if it present at even index
'''a = input('Enter a string')
b = ''

for i in range(0,len(a),2):
        if 'A'<=a[i]<='Z':
            b = b + a[i]
print(b)'''

#WAP to reverse a string without using slicing

'''a = input('Enter a String')
b = ''

#for i in a:
    #b = i+b
#for i in range(0,len(a)):
 #   b = b + a[len(a)-1-i]
for i in range(len(a)-1,-1,-1):
    b= b + a[i]
print(b)'''

#WAP to find length of dictionary without using len function

'''a = eval(input('Enter a dictionary'))
count= 0
for i in a:
    count +=1

print('Length of dictionary :',count)'''

#WAP to remove all the duplicates values in a list
'''a = eval(input('Enter a List\n'))
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)'''

#WAP to extract all the key value pair from thedictionary only if keys are of string data typeand values are interger data type

'''a = eval(input('Enter a dictionary'))
b = {}
for i in a:
    if type(i)==str and type(a[i])==int:
        b[i] = a[i] #for dict add data is like that
print(b)'''
























