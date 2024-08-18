from overrides import overrides
import WaterAnimal


class Whale(WaterAnimal):
    @staticmethod
    def chase_sailboats(self):
        print("\n- The Whale is chasing the sailboats!")

    @overrides
    def swim_to(self):
        print("\n- The Whale is swimming!")

    @overrides
    def eat(self):
        print("\n- The Whale is eating!")

    @overrides
    def sleep(self):
        print("\n- The Whale is sleeping!")
