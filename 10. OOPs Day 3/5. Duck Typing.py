# Duck Typing Example:



class Duck:
    def sound(self):
        print("Quack Quack")
class Dog:
    def sound(self):
        print("Woof Woof")
#MainScript
def make_sound(animal):
    animal.sound()

#Create individual object
d = Duck()
dog = Dog()
make_sound(d)
make_sound(dog)