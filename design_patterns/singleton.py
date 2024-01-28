from typing import Any

class MetaClass(type):
    """This is singleton design pattern."""
    
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

a = A()

print(f"Creating object :{a}")
    
    