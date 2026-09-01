# Create the following classes:

# * `Animal`
# * `Dog(Animal)`

# Both classes have a method `sound()`.

# * `Animal.sound()` prints `"Animal Sound"`
# * `Dog.sound()` prints `"Dog Barks"`

# Create a `Dog` object and call `sound()`.

# Also print the MRO.


class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        
dog = Dog()
dog.sound()
# Animal.sound(dog)
print(Dog.mro())
