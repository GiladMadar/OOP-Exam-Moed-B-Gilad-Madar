from abc import ABC, abstractmethod
import Animal
from overrides import overrides


class LandAnimal(ABC, Animal):
    @abstractmethod
    def move_to(self):
        pass

    @overrides
    def eat(self):
        pass

    @overrides
    def sleep(self):
        pass
