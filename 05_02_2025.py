#example of class
'''
class Bank:
    bname = 'hdfc'
    bloc = 'bangalore'
    bid = 123456789

    def __init__(self,cname,cloc,cid):
        self.cname = cname
        self.cloc = cloc
        self.cid = cid

c1 = Bank('prince','bang',123)   #In this positonal argument present
c2 = Bank('dilip','delhi',456)

print(c1.cname,c1.bname,c1.bloc,c1.bid,c1.cloc,c1.cid)
print(c2.cname,c2.bname,c2.bloc,c2.bid,c2.cloc,c2.cid)
'''

class Company:
    com_name = 'TCS'
    com_add = 'Noida'

    def __init__(self,e_name,e_id):
        self.e_name = e_name
        self.e_id = e_id
e1 = Company('prince',1245)
e2 = Company('brave',2367)
e3 = Company('google',7856)

print(e1.com_name,e1.com_add,e1.e_name,e1.e_id)
print(e2.com_name,e2.com_add,e2.e_name,e2.e_id)
print(e3.com_name,e3.com_add,e3.e_name,e3.e_id)
