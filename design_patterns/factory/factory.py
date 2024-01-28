""" Factory Design Pattern. """


class A(object):
    def __init__(self) -> None:
        pass
    
    def MethodA(self):
        print("Printing i'm a Method A:")
        
class B(object):
    def __init__(self) -> None:
        pass
    
    def MethodB(self):
        print("Printing i'm a Method B:")
        
def get(obj = ""):
    objs = dict(a =A(),b=B())
    return objs[obj]

a = get("a")
a.MethodA()
b = get("b")
b.MethodB()


#Example : 2-------------------------------------------

# Shape interface
class Shape:
    def draw(self):
        pass

# Concrete Circle class implementing Shape interface
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

# Concrete Rectangle class implementing Shape interface
class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

# Shape Factory
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")

# Client code
if __name__ == "__main__":
    # Creating a Shape factory
    factory = ShapeFactory()

    # Creating Circle
    circle = factory.create_shape("Circle")
    circle.draw()

    # Creating Rectangle
    rectangle = factory.create_shape("Rectangle")
    rectangle.draw()

