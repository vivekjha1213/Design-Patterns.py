    
#Method :4

from typing import Any


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
    
    
    
e= E()
print(f"object:{e}")
