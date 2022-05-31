from graphics import *
import random
import time

class Player():

    def __init__(self,win,p, i):
        self.p = p
        self.win = win
        self.im = Image(p, i)
        self.im.draw(win)


    def getPos(self):
        self.p
        
    def run(self, ball):
        directionx = ball.getPos().getX() - self.p.getX()
        directiony = ball.getPos().getY()- self.p.getY()
        self.p.move(directionx/50, directiony/50)
        self.im.move(directionx/50, directiony/50)
    
        
        
    
        
        
    
