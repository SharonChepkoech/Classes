
# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

# from pydoc import pager

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circle_area(self):
        self.area = (3.14)*(self.radius**2)
        return self.area

    def circle_circumference(self):
        self.circumference = (2*(3.14))*(self.radius)
        return self.circumference
# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
class Square:
    def __init__(self,side):
        self.side = side
    def square_area(self):
        area = (self.side**2)
        return area

    def square_perimeter(self):
        perimeter = (self.side * 4)
        return perimeter

# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,width,length):
        self.legth = length 
        self.width = width
    def rectangle_area(self):
        area = (self.width * self.legth)
        return area
    def rectabgle_perimeter(self):
        perimeter = (2*(self.width + self.legth))
        return perimeter
    
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def sphere_surface_area(self):
        self.surface_area = (4*(3.14)*(self.radius**2))
        return self.surface_area
    
    def sphere_volume(self):
        self.volume = (4/3 * (3.14 * self.radius**3))
        return self.volume