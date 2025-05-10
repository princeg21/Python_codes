#Single Value Inhertance
'''
class A:
    a = 10
    b = 20

    def __init__(self,c,d):
        self.c = c
        self.d = d

oa = A(100,200)
print(oa.c,oa.d)

class B(A):
    m = 2000
    n = 3000

    def __init__(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r

ob = B(1,2,3)
print(ob.a,ob.b,ob.p,ob.q,ob.r)
'''

#example 2
#-----------super class-----------
class Animal:

    def sound(self):
        print('animal makes sound')
#-----------subclass--------------
class Dog(Animal):

    def sound(self):
        print('dog will make sound')
d1 = Animal()
dog = Dog()
dog.sound()
d1.sound()
