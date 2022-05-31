from graphics import*

class Ball():
    def __init__(self,win,p):
        self.p = p
        self.win = win
        self.im = Image(p, "Ball.png")
        self.im.draw(win)

    def getPos(self):
        return self.p

    def movetogoal(self, SG):
        movex = 1150 - self.getPos().getX() 
        movey = 380 - self.getPos().getY()
        self.p.move(movex/50, movey)
        self.im.move(movex/50, movey)
            
            
        
