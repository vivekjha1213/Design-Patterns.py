#Method:3
from typing import Any


class C(object):
    def __new__(cls,*args: Any, **kwargs: Any) -> Any:
        print("Creating a Object:")
        return super(C,cls).__new__(cls,*args,**kwargs)
    
    
    
c = C()
print(f"object:{c}")