'''How does abstraction in the Shape class facilitate working with different types of shapes 
   (e.g., Circle and Rectangle), and what are the benefits of this approach?'''

from abc import ABC, abstractmethod
import math

#-----------------------------Abstract Class---------------------------#
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(Self):
        pass

#------------------------------Circle Class----------------------------#
class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def draw(self):
        print(f"Circle {self.radius}")  

    def area(self):
        return math.pi * (self.radius ** 2)

#----------------------------Rectangle Class----------------------------#
class Rectangle(Shape):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def draw(self):
        print(f"Rectangle width is {self.width} and hight is {self.hight}")

    def area(self):
        return self.width * self.hight

def draw_and_cal_area(shape):
    shape.draw()
    print(f"Area : {shape.area()}")

#---------------------------Main Class-------------------------------------#
def main():
    circle = Circle(radius=5)
    rectangle = Rectangle(width=5, hight=5)

    print("Shape Information")
    draw_and_cal_area(circle)
    draw_and_cal_area(rectangle)

if __name__ == "__main__":
    main()        
