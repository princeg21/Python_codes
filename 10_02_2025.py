#constructor & method chaining

class Bank1:
    bname = 'hdfc'
    bloc = 'bng'
    bifsc = 'HD000'
    
    def __init__(self,cname,cno):
        self.cname = cname
        self.cno = cno
        
    def display(self):
        print(self.cname,self.cno)
        
class Bank2(Bank1):
    bname = 'sbi'
    bloc = 'bng'
    bifsc = 'sb000'
    
    def __init__(self, cname, cno,cac):
        #super().__init__(cname, cno) #1st type syntax
        Bank1.__init__(self, cname, cno)#3rd types syntax
        # self.cname = cname  #replacable
        # self.cno = cno      #replacable
        self.cac = cac
        
    def displayB2(self):
        # super().display()
        Bank1.display(self)
        print(self.cname,self.cno,self.cac)

ob1 = Bank1('karan', 123445467)
ob1.display()
obj1 = Bank2('keshav', 192578687, 111222222444)
obj1.displayB2()
