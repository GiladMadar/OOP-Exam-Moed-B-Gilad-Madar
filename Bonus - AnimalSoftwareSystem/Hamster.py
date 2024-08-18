from overrides import overrides
import LandAnimal


class Hamster(LandAnimal):
    @staticmethod
    def plan_escape(self):
        print("\n- The Hamster is planning escape!")

    @overrides
    def move_to(self):
        print("\n- The Hamster is moving!")

    @overrides
    def eat(self):
        print("\n- The Hamster is eating!")

    @overrides
    def sleep(self):
        print("\n- The Hamster is sleeping!")
