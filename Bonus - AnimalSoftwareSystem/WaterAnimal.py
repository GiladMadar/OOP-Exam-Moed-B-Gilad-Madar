from abc import ABC, abstractmethod
from overrides import overrides
import Animal


class WaterAnimal(ABC, Animal):
    @abstractmethod
    def swim_to(self):
        pass

    @overrides
    def eat(self):
        pass

    @overrides
    def sleep(self):
        pass
