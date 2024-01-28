#Method:1
from typing import Any


class A(object):
    def __init__(self) -> None:
        pass
    
#Method:2
class B(object):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        return super(B,cls).__call__(cls,*args, **kwargs)
    
#Method:3
class C(object):
    def __new__(cls,*args: Any, **kwargs: Any) -> Any:
        print("Creating a Object:")
        return super(C,cls).__new__(cls,*args,**kwargs)
    
    
    def __init__(self,*args, **kwargs) -> None:
        print("Creating Instance of Class.")
        super(C,self).__init__(*args,**kwargs)
        
#Method :4

class D(type):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        print("Creating an Object:")
        instance = super(D, cls).__call__(*args, **kwargs)
        return instance
    
    def __init__(cls, name, bases, attrs) -> None:
        print("Initializing an Object:")
        super(D, cls).__init__(name, bases, attrs)

class E(metaclass=D):
    pass
    
    
    

#creating Instance of the class.
# a = A()
# print(f"class:{a}")
# b = B()
# print(f"object:{b}")
#c = C()
#print(f"object:{c}")
e= E()
print(f"object:{e}")
