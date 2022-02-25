from graphics import*
from Button import*
from math import*

def fullSplit(f, splitters):

    final = []

    store = ""
    for a in f:
        if a in splitters:
            final.append(store)
            store = ""
        else:
            store += a
    final.append(store)
    return final


def calcy(f, num):
    
    result = f
    if "+" in f or "-" in f or "*" in f or "/" in f:
        for i in f:
            if "+" in f :
                i = f.split("+")
                result = calcy(i[0], num) + calcy(i[1],num)
                return result
            elif "-" in f:
                i = f.split("-")
                result = calcy(i[0], num) - calcy(i[1],num)
                return result
            elif "*" in f:
                i = f.split("*")
                result = calcy(i[0], num) * calcy(i[1],num)
                return result
            else:
                i = f.split("/")
                if calcy(i[1],num) == 0:
                    return 0
                else:
                    result = calcy(i[0], num) / calcy(i[1],num)
                    return result


    
    if "sqrt(x)" == f:
       if num < 0:
           return 0
       else:
            return sqrt(num)
    elif "x^2" == f:
        return num**2
    elif "sin(x)" == f:
        return sin(num)
    elif "e^x" == f:
        return e**num
    elif "cos(x)" == f:
        return cos(num)
    elif "log(x)" == f:
        if num <= 0:
            return 0
        else:
            return log(num)
    elif "x" == f:
        return num
    elif f.isnumeric():
        return int(f)
    
    
        

def main():
    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function you would like to graph")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)

    yAxis = Line(Point(150,200), Point(150,650))
    yAxis.draw(win)
    xAxis = Line(Point(150,500), Point(650,500))
    xAxis.draw(win)

    funText = Text(Point(200,650), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,650),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(550,650), 75)
    quitB = Button(win, 'red', "QUIT", Point(400,720), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()

            scale = 50

            points = []

                
            if not "sqrt" in f or  "log" in f:
                yAxis.undraw()
                yAxis = Line(Point(400,200), Point(400,650))
                yAxis.draw(win)

                for i in range(500):
                    x = i + 400
                    y = 500 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))
                
                for p in points:
                    p.draw(win)
            
    
            else:
                for i in range(500):
                    x = i + 150
                    y = 500 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))

                for p in points:
                    p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break

       

        
            

if __name__ == "__main__":
    main()
