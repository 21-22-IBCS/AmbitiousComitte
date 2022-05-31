from graphics import*
from Button import*
from Player import*
from Ball import*
from soccergoal import*
import math
import time
import random




def main():
    
    win = GraphWin("Soccer Simulation 2022", 1400, 800)
    quiB = Button(win, "grey", "Quit", Point(1300,200), 50)
    Move = Button(win, "cyan", "Move", Point(1300,100),50)
    Goal = Button(win, "red", "Goal", Point(1300,50),50)

    background = Image(Point(600,380), "Goal.png") 
    background.draw(win)

    Mx = random.randint(50,1100)
    My = random.randint(50,710)
    M = Point(Mx,My)
    player = Player(win, M , "Messi.png")
    
    Bax = random.randint(50,1100)
    Bay = random.randint(50,710)
    Ba = Point(Bax,Bay)
    ball = Ball(win, Ba)

    sg = Point(1150,380)
    SG = soccergoal(win, sg)

    while True:
        m = win.getMouse()
        if quiB.isClicked(m):
            win.close()
            break
        
        if Move.isClicked(m):
            while ball.getPos() != player.getPos():
                time.sleep(.01)
                player.run(ball)
                if player.getPos() == ball.getPos():
                    break
                else:
                    continue
            
            
               
        if Goal.isClicked(m):
            while True:
                time.sleep(.01)
                ball.movetogoal(SG)

       
                
                
                

               



if __name__ == "__main__":
    main()


    Ax = random.randint(50,1100)
    Ay = random.randint(50,710)
    A = Point(Ax,Ay)
    P2 = Player(win, A , "Aquero.png")

    Vx = random.randint(50,1100)
    Vy = random.randint(50,710)
    V = Point(Vx,Vy)
    P3 = Player(win, V , "Virgil.png")

    Rx = random.randint(50,1100)
    Ry = random.randint(50,710)
    R = Point(Rx,Ry)
    P4 = Player(win, R , "Ronaldo.png")

    Kx = random.randint(50,1100)
    Ky = random.randint(50,710)
    K = Point(Kx,Ky)
    P5 = Player(win, K , "Kane.png")

    Max = random.randint(50,1100)
    May = random.randint(50,710)
    Ma = Point(Max,May)
    P6 = Player(win, Ma , "Mane.png")

    Gx = random.randint(50,1100)
    Gy = random.randint(50,710)
    G = Point(Gx,Gy)
    P7 = Player(win, G , "Gulit.png")

    Sx = random.randint(50,1100)
    Sy = random.randint(50,710)
    S = Point(Sx,Sy)
    P8 = Player(win, S , "Salah.png")

