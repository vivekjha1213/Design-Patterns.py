class Slots(object):
    __slots__ = ["name"]

    def __init__(self, name) -> None:
        self.name = name

# Create an instance of the Slots class
slot = Slots(name="vivek")

# Access the attribute defined in __slots__
print(slot.name)  # Output: vivek

# Attempt to create a new attribute (will raise an AttributeError)
# slot.age = 999999  # Uncommenting this line will result in an AttributeError

# TypeError: 'Slots' object has no attribute 'age'
