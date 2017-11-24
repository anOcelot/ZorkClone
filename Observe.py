from abc import ABC

#Basic implementation of the observable pattern
class Observable(ABC):

    #constructor
    def __init__(self):
        self.observers = []

    #used to attack an object to its observer
    def attach(self, observer):
        self.observers.append(observer)

    #used to detach an object from an observer, if need be
    def detach(self, observer):
        self.observers.remove(observer)

    #used to notify all observers of change in state
    def notify(self):
        for observer in self.observers:
            observer.update()


#basic abstract observer class. As an abstract class, it can be
#inherited by any game object.
class Observer(ABC):


    #defer to the heir class
    def update(self):
        pass