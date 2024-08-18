from overrides import overrides
import WaterAnimal


class GoldFish(WaterAnimal):
    @staticmethod
    def hide_from_cat():
        print("\n- The Gold Fish is hiding from the cat!")

    @overrides
    def swim_to(self):
        print("\n- The Gold Fish is swimming!")

    @overrides
    def eat(self):
        print("\n- The Gold Fish is eating!")

    @overrides
    def sleep(self):
        print("\n- The Gold Fish is sleeping!")
