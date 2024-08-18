from overrides import overrides
import LandAnimal


class Dog(LandAnimal):
    @staticmethod
    def chase_cars(self):
        print("\n- The Dog is chasing cars!")

    @staticmethod
    def droll(self):
        print("\n- The Dog is drooling!")

    @overrides
    def move_to(self):
        print("\n- The Dog is moving!")

    @overrides
    def eat(self):
        print("\n- The Dog is eating!")

    @overrides
    def sleep(self):
        print("\n- The Dog is sleeping!")
