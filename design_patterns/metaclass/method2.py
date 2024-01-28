#Method:2
from typing import Any


class B(object):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        return super(B,cls).__call__(cls,*args, **kwargs)
    
    
    
b = B()
print(f"Object 3:{b}")