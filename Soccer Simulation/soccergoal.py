from graphics import*

class soccergoal():
    def __init__(self,win,p):
        self.p = p
        self.win = win
        self.im = Image(p, "soccergoal.png")
        self.im.draw(win)

    def getPos(self):
        return self.p
