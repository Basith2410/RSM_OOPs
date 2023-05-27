# 5. Shape Class Hierarchy:
# You are creating a geometry library. You create a base class called Shape with an abstract method called calculate_area(). 
# You derive subclasses for different shapes: Circle, Rectangle, and Triangle. 
# In the Circle class, you add an attribute radius and implement the calculate_area() method for circles. 
# In the Rectangle class, you add attributes length and width and implement the calculate_area() method for rectangles. 
# In the Triangle class, you add attributes base and height and implement the calculate_area() method for triangles. 
# You create instances for a circle named myCircle, a rectangle named myRectangle, and a triangle named myTriangle. 
# You invoke the calculate_area() method for each shape to calculate their respective areas.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(x):
        pass
    
class Circle(Shape):
    def __init__(x,radius):
        x.radius = radius
    def calculate_area(x):
        return 3.14159 * x.radius**2

class Rectangle(Shape):
    def __init__(x,l,b):
        x.l = l
        x.b = b
    def calculate_area(x):
        return x.l*x.b 

class Triangle(Shape):
    def __init__(x,b,h):
        x.b = b
        x.h = h
    def calculate_area(x):
        return 1/2*x.b*x.h 
    
print("//Area//")
myCircle = Circle(5)
circle_area = myCircle.calculate_area()
print("Circle Area:", circle_area)
print("")
myRectangle = Rectangle(10,5)
rectangle_area = myRectangle.calculate_area()
print("Rectangle Area:", rectangle_area)
print("")
myTriangle = Triangle(10,5)
triangle_area = myTriangle.calculate_area()
print("Triangle Area:", triangle_area)
