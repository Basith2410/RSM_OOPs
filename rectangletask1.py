# 1. Rectangle Class:
# Harshini is creating a computer-aided design (CAD) software. She needs to represent rectangles in her program. 
# She creates a class called Rectangle with attributes length and width.She should implement methods to calculate 
# the area and perimeter of the rectangle. For that, she creates instances for rectangles named smallRectangle 
# and largeRectangle and invokes the methods to calculate their respective areas and perimeters. Help her work on this task.

#length = l, width = w
#large= l , small = s
class Rectangle():
    def __init__(x,l,w):
        x.l = l
        x.w = w
    
    def rectangle_area(x):
        return x.l * x.w
    
    def rectangle_perimeter(x):
        return 2* (x.l + x.w)
    
smallRectangle = Rectangle(4,3)
largeRectangle = Rectangle(10,5)

s_area = smallRectangle.rectangle_area()
l_area = largeRectangle.rectangle_area()

s_perimeter = smallRectangle.rectangle_perimeter()
l_perimeter = largeRectangle.rectangle_perimeter()

print("// Area //")
print("Area of small rectangle: ", s_area)
print("Area of large rectangle: ", l_area)

print("\n// Perimeter //")
print("Perimeter of small rectangle: ", s_perimeter)
print("Perimeter of large rectangle: ",l_perimeter)

#Help successful, no need to mention :)