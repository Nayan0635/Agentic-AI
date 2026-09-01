## Question 4: Shape → Rectangle → Box

# * Class `Shape`

#   * Variables: `length`, `width`

# * Class `Rectangle` extends `Shape`

#   * Method: `area()`

# * Class `Box` extends `Rectangle`

#   * Variable: `height`
#   * Method: `volume()`

# Calculate and display both the area and volume.

# **Sample Output**

# ```
# Area = 50
# Volume = 200






class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
        return self.length * self.width
        
class Box(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volumn(self):
        return self.length * self.width * self.height
        
    def display(self):
        print(f"Area : {self.area()}")
        print(f"Volumn : {self.volumn()}")
        
        
# Main()
# len = 25
# wid= 2
# height = 4
shp = Box(25, 2, 4)
shp.display()