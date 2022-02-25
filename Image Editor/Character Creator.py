from graphics import*
from Button import*


def main():
    win = GraphWin("Currency Converter", 800, 800)
    face = Button(win, "white", "Face", Point(720, 50), 50)
    eye = Button(win, "white", "Eyes", Point(720, 150), 50)
    nose = Button(win, "white", "Nose", Point(720, 250), 50)
    mouth = Button(win, "white", "Mouth", Point(720, 350), 50)
    ear = Button(win, "white", "Ears", Point(720, 450), 50)
    hair = Button(win, "white", "Hair", Point(720, 559), 50)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)

    f = Circle(Point(330,300), 230)
    ey = Circle(Point(280,180), 20)
    ey2 = Circle(Point(380,180), 20)
    n = Polygon(Point(330,210), Point(360,250), Point(300,250))
    mo1 = Circle(Point(330,360), 80)
    mo2 = Rectangle(Point(250,280),Point(410,360))
    mo2.setFill("white")
    mo2.setOutline("white")
    mo3 = Line(Point(250,360),Point(410,360))
    mo4 = Rectangle(Point(310,360),Point(350,390))
    ea1 = Oval(Point(80,220),Point(100,320))
    ea2 = Oval(Point(560,220),Point(580,320))
    
    h = Line(Point(520,200),Point(540,100))
    

    m = win.getMouse()

    while True:
        if close.isClicked(m):
            break
        if face.isClicked(m):
            f.undraw()
            f.draw(win)

        if eye.isClicked(m):
            ey.undraw()
            ey2.undraw()
            ey.draw(win)
            ey2.draw(win)

        if nose.isClicked(m):
            n.undraw()
            n.draw(win)
            
        if mouth.isClicked(m):
            mo1.undraw()
            mo1.draw(win)
            mo2.undraw()
            mo2.draw(win)
            mo3.undraw()
            mo3.draw(win)
            mo4.undraw()
            mo4.draw(win)
            
        if ear.isClicked(m):
            ea1.undraw()
            ea1.draw(win)
            ea2.undraw()
            ea2.draw(win)
            
        if hair.isClicked(m):
            h.undraw()
            for i in range (20):
                h.draw(win)
                if i <7:
                    h=Line(Point(520-i*20,200-i*20),Point(540-i*20,100-i*20))
                elif i <=10:
                    h=Line(Point(520-i*20,200-i*10-10),Point(540-i*20-10,100-i*10-10))
                elif i<=20:
                    h=Line(Point(500-i*20,80+i*5),Point(540-i*20-50,10+i*5))

                    
                

        m=win.getMouse() 

if __name__ == "__main__":
    main()
