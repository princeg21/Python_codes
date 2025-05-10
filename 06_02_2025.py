#example for object method
'''
class company:
    com_name = 'wipro'
    com_loc = 'bangolore'
    com_ceo = 'harish'

    def __init__(self,e_name,e_id,e_sal):
        self.e_name = e_name
        self.e_id = e_id
        self.e_sal = e_sal

    def display(self):
        print(self.e_name,self.e_id,self.e_sal)

    def ch_e_id(self,new):
        self.e_id = new

    def ch_e_sal(self,new):
        self.e_sal = new

e1 = company('manoj',123,25000)
e2 = company('ashwin',234,30000)
e3 = company('anand',256,45000)

company.display(e1)
e1.display()
company.ch_e_id(e1,345)
company.display(e1)
e1.ch_e_id(12345)
e1.display()
e3.display()
e3.ch_e_id(787)
e3.ch_e_sal(50000)
e3.display()
'''

#Class method

class Library:
    lib_name = 'xyz'
    lib_add = 'banglore'

    def __init__(self,vname,vadd,vid):
        self.vname=vname
        self.vadd = vadd
        self.vid = vid

    def display(self):
        print(self.vname,self.vadd,self.vid)

    def ch_vname(self,new,new1,new2):
        self.vname = new
        self.vadd = new1
        self.vid = new2

    @classmethod
    def cl_display(cls):
        print(cls.lib_name,cls.lib_add)

    @classmethod
    def ch_lib_name(cls,new):
        cls.lib_name = new

v1 = Library('a','bng',123)
v2 = Library('b','mango',456)

v1.ch_vname('prince','jind',454)
v1.display()
#for object method call(2 ways)
Library.display(v1)
v1.display()
# for class method call(2 ways)
Library.cl_display()
v1.cl_display()
#modify of class member
Library.ch_lib_name('qwerty')
v1.cl_display()

# example 2
'''
class house:
    h_name ='navas'
    h_add = 'jind'

    def __init__(self,room_no,facility):
        self.room_no = room_no
        self.facility = facility

    def display(self):
        print(self.room_no,self.facility)

    def ch_facility(self,new):
        self.facility.append(new)

    @classmethod
    def ch_h(cls,name,add):
        cls.h_name = name
        cls.h_add = add
    
    @classmethod
    def cl_display(cls):
        print(cls.h_name,cls.h_add)

r1 = house(1,['tv','fridge'])
r2 = house(2,['washroom','tv'])

r1.ch_h('glory','noida')
house.cl_display()
r1.ch_facility('curtains')
r1.display()
'''





























