#creating function
def arclength():
    pi=22/7
    #taking the value of the radius and angle
    rad = float(input('Radius of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    arc_length = (pi*2*rad) * (angle/360)
    #printing the arc length
    print("Arc Length is: ", arc_length)

arclength()