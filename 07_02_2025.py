#WAP for static method
'''
class Bank:
    bname = 'sbi'
    bloc = 'bng'

    def __init__(self,cname,cphno,caccno,cbal):
        self.cname = cname
        self.cphno = cphno
        self.caccno = caccno
        self.cbal = cbal

    def obj_details(self):
        print(self.cname,self.cphno,self.caccno,self.cbal)

    def deposit(self,amt):
        self.cbal = self.add (self.cbal,amt)

    def withdraw(self,amt):
        if amt>self.cbal:
            print('insufficient balance')
        else:
            self.cbal = self.sub(self.cbal,amt)

    @classmethod
    def class_details(cls):
        print(cls.bname,cls.bloc)

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

c1 = Bank('a',12345677,99995643487,7000)
c1.obj_details()
c1.deposit(3000)
c1.obj_details()
c1.withdraw(5000)
c1.obj_details()
c1.withdraw(5000)
c1.obj_details()
'''

#WAP to perform addition of 2 numbers using object method, static method & class method

class addition:

    def add(self,a,b):
        print(a+b)


    @classmethod
    def cl_add(cls,a,b):
        print (a + b)

    @staticmethod
    def st_add(a,b):
        print(a+b)

a1 = addition()
a1.add(int(input('n1')),int(input('n2')))
a1.cl_add(int(input('n1')),int(input('n2')))
a1.st_add(int(input('n1')),int(input('n2')))
