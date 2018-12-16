# Mathematical point...
# two floating pt values, x and y
# would you want to group it into a list or a tuple?
# how about defining a new compound type?

class Point:
    pass

blank = Point()

# blank is now referenced to a new Point object.

blank.x = 3.0
blank.y = 4.0
print(blank.x)

# this is adding data to an instance of an obj using dot notation.
# this stuff is called attributes. 

#dot notation can be used as a part of any expression. 
print('(' + str(blank.x) + ', ' + str(blank.y) + ')')
distanceSquared = blank.x * blank.x + blank.y * blank.y 
print(distanceSquared)

# to find out if two references refer to the same object, use the is operator
p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
print(p1 is p2)

def printPoint(p): 
  print('(' + str(p.x) + ', ' + str(p.y) + ')')

# this is known as shallow equality because it compares only the references
# not the content of the objects.

# to compare the contents of the objects (deep equality)
# could write a function for this!

def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

print(samePoint(p1, p2))

# What if we wanted to represent a rectangle?
# Let's assume rectangles are oriented vertically or horizontally. 
# Could specify the center and the size (two coordinates and then width and height)
# Could specify one corner and the size. 
# Conventional choice is to specify upper left corner and the size.

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0

# embed an object in an object. 

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# functions can return instances. 

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y - box.height/2.0
    return p

# the above code just made a point, calculated the center from the rectangle provided
# and then returned the point marking the center 
center = findCenter(box)
printPoint(center)

# objects are mutable

def growRect(box, dwidth, dheight):
    box.width = box.width + dwidth
    box.height = box.height + dheight

bob = Rectangle()
bob.width = 100.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0

growRect(bob, 50, 100)

def moveRect(rectangle, dx, dy):
    rectangle.corner.x = rectangle.corner.x + dx
    rectangle.corner.y = rectangle.corner.y + dy

print(bob.width)
moveRect(bob, 5, 5)
print(bob.corner.x)

# copying an object is an alternative to aliasing. 
# copy module has a function called copy that duplicates objects

# when you copy something simple like a point, which doesn't contain
# embedded objects, copy is sufficient. this is "shallow copying"

# For the rectangle, which has a reference to a point, copy will copy
# the reference to the point object, so both the old and the new rect
# will end up referring to the same point. 

# you'd want to use copy.deepcopy(box) for this. 

def moveRectCopy(rectangle, dx, dy):
    newRect = copy.deepcopy(rectangle)
    newRect.corner.x = newRect.corner.x + dx
    newRect.corner.y = newRect.corner.y + dy
    return newRect

