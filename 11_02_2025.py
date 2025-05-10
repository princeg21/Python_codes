# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:11:16 2025
topic: Multi-level inheritance
@author: gargp
"""
# =============================================================================
# class A:
#     a = 10
#     b = 20
#     
#     def __init__(self,c):
#         self.c = c
#         
# class B(A):
#     
#     def __init__(self, c,d,e):
#         super().__init__(c)
#         self.d = d
#         self.e = e
#         
#     m = 100
#     n = 200
#     
# class C(B):
#     p = 1000
#     q = 2000
#     
# class D(C):
#     x = 1
#     y = 2
#     
# oa = A(8)
# ob = B(8,9,10)
# print(A.a,A.b)
# print(B.a,B.b,B.m,B.n)
# print(C.a,C.b,C.m,C.n,C.p,C.q)
# print(D.a,D.b,D.m,D.n,D.p,D.q,D.x,D.y)
# =============================================================================

#Example 2 =============================================================================
# class Basicd:
#     
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         
#     def displayd(self):
#         print(self.name,self.age)
#         
# class Education(Basicd):
#     
#     def __init__(self, name, age, degree):
#         super().__init__(name, age)
#         self.degree = degree
#         
#     def displayedu(self):
#         print(self.degree)
#         
# class Resume(Education):
#     
#     def __init__(self,name,age,degree,company,years):
#         super().__init__(name, age, degree)
#         self.company = company
#         self.years = years
#         
#     def displayres(self):
#         self.displayd()
#         self.displayedu()
#         print(self.company,self.years)
#         
# mres = Resume('Prince', 28, 'B. Tech', 'Wipro', 3)
# mres.displayres()        
# =============================================================================

#Example 3 =============================================================================
# class Engine:
#     
#     def start(self):
#         print('bike started')
#         
# class Bike(Engine):
#     
#     def go(self):
#         print('bike is running')
#         
# class Ktm(Bike):
#     
#     def gofast(self):
#         print('bike is going fast')
#         
# duke = Ktm()
# duke.start()
# duke.go()
# duke.gofast()
# =============================================================================
'''topic: multiple inheritance'''

class Engine:
    
    def start(self):
        print('started')
        
class Wheels:
    
    def rotate(self):
        print('wheels are rotating')

class Brake:
    def stop(self):
        print('car stopped')
        
class Car(Engine,Wheels,Brake):
    
    def drive(self):
        print('its running')

car = Car()
car.start()
car.rotate()
car.drive()
car.stop()
