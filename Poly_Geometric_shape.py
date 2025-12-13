class Shape():
    def describe(self):
        return 'A shape is the external boundary, form, or outline of an object, defined by its edges, curves, and vertices, separate from its color or texture, like a square, circle, or sphere, representing 2D or 3D forms we see in the world'
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def describe(self):
        return f'A circle is a perfectly round, two-dimensional shape where every point on its continuous curved line is the exact same distance from a central point, having no corners or edges, like a coin or wheel. \nThe radius of this circle is {self.radius} cm '
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def describe(self):
        return f'A rectangle is a flat, four-sided shape with four right angles, where opposite sides are parallel and equal in length. \nThe length and width of this rectangle are {self.length} cm and {self.width} cm,respectively'

s=[Circle(4),Rectangle(5,4),Rectangle(9,4)]
for i in s:
    print(i.describe())