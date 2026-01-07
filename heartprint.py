import math
from graphics import *
window = GraphWin('Cool Heart', 640, 360)
window.setBackground("black")
Arcp = []


width = 80
radius = width/4
midpoint = (width/2,100)
cc1 = (midpoint[0] - radius, midpoint[1])# center of circle 1
cc2 = (midpoint[0] + radius, midpoint[1])# center of circle 2

quadrants = 10

#append cc1 coordinates
for i in range(1, quadrants + 1, 1):
    angle = i * 180/quadrants #degrees
    angle = angle * math.pi/180 #radians
    ydis = -round(math.sin(angle) * radius)
    xdis = round(math.cos(angle) * radius)

    Arcp.append(Point(int(cc1[0] + xdis), int(cc1[1] + ydis)))

#append bottom middle point
Arcp.append(Point(width/2, 160))

#append cc2 coordinates
for i in range(0, quadrants + 1, 1):
    angle = i * 180/quadrants #degrees
    angle = angle * math.pi/180 #radians
    ydis = -round(math.sin(angle) * radius)
    xdis = round(math.cos(angle) * radius)

    Arcp.append(Point(int(cc2[0] + xdis), int(cc2[1] + ydis)))


heart = Polygon(Arcp)
heart.draw(window)
heart.setFill("red")
heart.move(320 - width/2, 180 - 100)

window.getMouse()
window.close()