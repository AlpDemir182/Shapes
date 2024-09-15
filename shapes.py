import pgzrun
width = 600
height = 400

def draw():
    screen.clear()
    rectcolor = "blue"
    rect = Rect((50,50), (100,50))
    screen.draw.filled_rect(rect,rectcolor) 

    rect2color = "red"
    rect2 = Rect((200,50), (200,50))
    screen.draw.filled_rect(rect2,rect2color)

    circlecolor = "green"
    circlecoord = (300,200)
    radius = 50
    screen.draw.filled_circle(circlecoord,radius,circlecolor)

    linecolor = "yellow"
    linestart = (450,50)
    lineend = (550,150)
    screen.draw.line(linestart,lineend,linecolor)

pgzrun.go()