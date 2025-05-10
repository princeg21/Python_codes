#WAP to get the following output input-> [200,60,40,100]  output->[200,340,360,300] 

'''a = eval(input('Enter a list\n'))
b = []
sumi = sum(a)
for i in a:
    b.append(sumi-i)
print(b)

2nd method
for i in a:
    sum = 0
    for j in a:
        if i!=j:
            sum+=j
    b.append(sum)
print(b)
'''
#WAP to get the following output input-> 'aaabbaccbb'; output -> a4b4c2

'''a = input('Enter a String\n')
b = ''

for i in a:
    if i not in b:
        count = 0
        for j in a:
            if i ==j:
                count = count +1
        b = b + i + str(count)
print(b)'''

# kabab is love; reverse the string & count the vowel output->{'kabab':['babak',2,'bbk'],'is':['si',1,'i'],'love':['evol',2,'lv']}

a = input('Enter a string\n')
b = {}

for i in a.split():
    count = 0
    for j in i:
        if j in 'aeiouAEIOU':
            count = count +1
    b[i] = [i[::-1],count,i[::2]]
print(b)


















