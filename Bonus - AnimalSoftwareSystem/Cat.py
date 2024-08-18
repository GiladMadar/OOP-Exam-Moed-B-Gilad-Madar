from overrides import overrides
import LandAnimal


class Cat(LandAnimal):
    @staticmethod
    def overthrow_humans(self):
        print("\n- The Cat is overthrowing humans!")

    @staticmethod
    def cough_up_furballs(self):
        print("\n- The Cat is coughing up furballs!")

    @overrides
    def move_to(self):
        print("\n- The Cat is moving!")

    @overrides
    def eat(self):
        print("\n- The Cat is eating!")

    @overrides
    def sleep(self):
        print("\n- The Cat is sleeping!")
