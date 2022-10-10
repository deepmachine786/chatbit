# using the User Defined Exception 

# User Defind Exception Are Sub class of Exception ....




# class MyError(BaseException):
#    def __init__(self, name:str="Myname") -> None:
#         self.name = name 

# try:
#     raise MyError()
# except MyError as e:
#     print(" Get The New Execption Occured ",e.name)

# def func(num):
#     if num==0 or num==1:
#         return num
#     return func(num-1) + func(num-2)

# print(func(20))
from dataclasses import dataclass
from functools import total_ordering, recursive_repr
import functools
# @dataclass(fronze=True) # if we use fronze=true then data will immutable we cant change 
# class Name:
#     name: str
#     age : int 

# # if we want to cust=oe the attribute in the dataclass the we use __post_init__(
# # costrucer ..)
#     def __post_init__(self):
#         self.disc = self.name+" "+str(self.age)

#     def __eq__(self,other):
#         return self.age > other.age

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         self.__name = __value
@recursive_repr
class Names(object):
    def __init__(self) -> None:
        self.name = " N"
        self.age = 22

    def __ge__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age
    def __setattr__(self, __name: str, __value) -> None:
        super().__setattr__(__name,__value)

obj = Names(object)
obj.name = "34"
print(obj.name)
print(dir(obj))
print(dir(Names))

print(dir(functools))