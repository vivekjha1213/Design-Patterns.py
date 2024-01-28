from typing import Any

class MetaClass(type):
    """This is singleton design pattern.
    """
    
    _instance = {}
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """if instance already exits dont create.."""
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass,cls).__call__(*args, **kwds)
            
            return cls._instance[cls]
        
class A(metaclass = MetaClass ):
    
    def __init__(self) -> None:
        pass



#creating a obj

obj = A()
print(f"Creating object :{obj}")

#if already created instance it will return None.

# Creating object :<__main__.A object at 0x105ef57d0>
# Creating object 1 :None
obj1 = A()
print(f"Creating object 1 :{obj1}")
