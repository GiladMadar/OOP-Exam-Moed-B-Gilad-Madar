import Animal
import LandAnimal
import WaterAnimal
import GoldFish
import Whale
import Cat
import Dog
import Hamster


#   Classes Tests : Animal: { WaterAnimal: [GoldFish, Whale], LandAnimal: [Hamster, Dog, Cat] }
def main():
    # Test Water Animals
    goldfish = GoldFish
    goldfish.swim_to()
    goldfish.eat()
    goldfish.sleep()
    goldfish.hide_from_cat()

    whale = Whale
    whale.swim_to()
    whale.eat()
    whale.sleep()
    whale.chase_sailboats()

    # Test Land Animals
    cat = Cat
    cat.move_to()
    cat.eat()
    cat.sleep()
    cat.overthrow_humans()
    cat.cough_up_furballs()

    dog = Dog
    dog.move_to()
    dog.eat()
    dog.sleep()
    dog.chase_cars()
    dog.droll()

    hamster = Hamster
    hamster.move_to()
    hamster.eat()
    hamster.sleep()
    hamster.plan_escape()


#   Performing main Classes Tests
if __name__ == "__main__":
    main()
