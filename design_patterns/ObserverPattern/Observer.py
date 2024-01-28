"""Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically."""


class Observer():
    def update(self,message):
        pass
    
class ConcreteObserver(Observer):
    def update(self,message):
        print(f"Received message: {message}")


obj = ConcreteObserver()
print(obj)