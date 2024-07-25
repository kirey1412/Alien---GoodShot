import pgzrun, random

TITLE="Good Shot Game"
WIDTH=400
HEIGHT=400

message="Empty"
alien=Actor("alien")
alien.pos=200,200
score=0
def draw():
    global score, message
    screen.fill("navy")
    alien.draw()
    screen.draw.text("Score:"+str(score),center=(360,100), fontsize=30, color="red")
    screen.draw.text(message, center=(355,70), color="red")

def on_mouse_down(pos):
    global score, message
    if alien.collidepoint(pos):
        placealien()
        score+=1
        message="Good Shot"
    else:
        message="Bad Shot"


def placealien():
    alien.x=random.randint(50,350)
    alien.y=random.randint(50,350)


pgzrun.go()