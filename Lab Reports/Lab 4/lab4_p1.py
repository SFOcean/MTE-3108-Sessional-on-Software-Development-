class Point(object):
    """represents a point in 2-D space"""
class Rectangle(object):
    """Represents a rectangle.
        attributes: width, height, corner"""
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()        #A point in 2D space
#Taking Initial x,y as input
initial_x = input("Enter initial x cordiante = ")
initial_y = input("Enter initial y cordinate = ")
#Using Methods and type casting for calculation
box.corner.x = float(initial_x)
box.corner.y = float(initial_y)
print ("Initial Box Corner Set: ")
print ("Initial x = " + str(box.corner.x))
print ("Initial y = " + str(box.corner.y))
dx = input("Enter dx = ")
dy = input("Enter dy = ")
#Calling move_rectangle function
move_rectangle(box, float(dx), float(dy))
print ("New Box Corner: ")
print ("x = " + str(box.corner.x))
print ("y = " + str(box.corner.y))