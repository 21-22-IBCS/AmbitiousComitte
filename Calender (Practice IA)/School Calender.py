from graphics import*
from Button import*

def main():
    # the frame for the main screen
    win = GraphWin("School Event", 800, 500)
    #800 is the point the window will reach to 
    #500 is the point the window will reach to vertically
    background = Image(Point(400,250), "background.gif")
    background.draw(win)
    
    # position of three options buttons that user can choose
    tutorial = Button(win, "white", "Tutorial", Point(400, 100), 85)
    community = Button(win, "white", "Community Meeting", Point(400, 250), 85)
    flex = Button(win, "white", "FLEX", Point(400, 400), 85)
    quitt = Button(win, "grey", "Quit", Point(750,450),50)
            
    filez = open("Event.txt", "r")
    z = filez.read()

    fe = open("Event.txt", "r")
    
    def flexlocation(x):
        G = ''
        B = ''
        Y = ''
        s = '\n'
        for x in fe:
            if "Yellow" in x:
                if "Kemper Theatre" in x:
                    Y = Y + "Yellow: Kemper Theatre"
                else:
                    Y = Y + "Yellow: Atrium"
            if "Blue" in x:
                if "Kemper Theatre" in x:
                    B = B +"Blue: Kemper Theatre"
                else:
                    B = B +"Blue: Atrium"
            if "Green" in x:
                if "Kemper Theatre" in x:
                    G = G +"Green: Kemper Theatre"
                else:
                    G = G +"Green: Atrium"
        return Y + s + B + s + G
    
    
    filem = open("Tutorial.txt", "r")
    fm = filem.read()

    def findday(x):
        word = "TUESDAY"
        if word in x:
            return "Event is on Tuesday, Wednesday, and Friday"
        else:
            return "Event is on Monday"
    

    def findlocation(x):
        if "the Kemper Theatre" in x:
            return ("The Community Meeting is in Kemper Theatre today")
        else:
            return ("The Community Meeting is in Chapel today")
        
    
    #find date for community/ flex
    def finddate(x):
        cd = ""
        for m in x:
           if m.isdigit(): #The date are always the first value in the text
               cd = cd + m
        return ("The date is " + cd[0] + cd[1])
    print('\n')

    #find date for tutorial
    num = finddate(fm)
    n = num.split()
    summ = 'The date are: '
    for i in n:
        if i.isdigit():
            summ = summ + str(int(i)) + "," + str(int(i)+1) + "," + str(int(i)+2)
            

    
    
        
    #Finding the time of the Flex Period
    l,m,k = z.partition("At") # partition is a method that can find the word before and after the key word
    #choose g because time always appear after "at"
    ksplit = k.split() #split the sentence into different string in a list
    timee = "The flex period is at " + ksplit[0] + " am" #the first string after "at" is always the time
    print(timee)
    print('\n')
    

    #Finding the time of the community meeting
    d,f,g = z.partition("From") # partition is a method that can find the word before and after the key word
    #choose g because time always appear after "at"
    gsplit = g.split() #split the sentence into different string in a list
    time = "The meeting time is on " + gsplit[0] + " am" #the first string after "at" is always the time

    
    #Finding the time of tutorial
    i,u,o = fm.partition("from") # partition is a method that can find the word before and after the key word
    #choose g because time always appear after "at"
    osplit = o.split() #split the sentence into different string in a list
    times = "Tutorial's time is " + osplit[0] + " pm" #the first string after "from" is always the time
    
    CM = time + "\n" + findday(z) + '\n' + finddate(z) + "\n" + findlocation(z)
    print(CM)
    print("\n")
    
    Tuto =  times + "\n" + findday(fm) + '\n' + str(summ) + "\n"
    print(Tuto)
    print('\n')


    flexlocate = flexlocation(fe)
    Flex = timee + "\n" + findday(z)  + "\n" + finddate(z) + "\n" + flexlocate
    print(Flex)
    

        
    
    m = win.getMouse()
    

    

    while True:
        if quitt.isClicked(m):
            win.close()
            break
        if tutorial.isClicked(m): #user choose to see tutorial event
            win.close()
            file = GraphWin("Tutorial", 300, 150)
            back = Button(file, "yellow", "back", Point(250, 30), 20)
            showfile = Button(file, "red", "detail", Point(80, 80), 40)
            readfile = Button(file, "white", "summary", Point(200, 80), 40)
            m2 = file.getMouse()
            if showfile.isClicked(m2):
                file.close()
                tc = GraphWin("Here is the Friday Flash for Tutorial", 1000, 750)
                back3 = Button(tc, "green", "back", Point(480, 100), 20)
                f = open("Tutorial.txt", "r")
                content = f.read()
                ptext = Text(Point(500, 350), content)
                ptext.draw(tc)
                m4 = tc.getMouse()
                if back3.isClicked(m4):
                    tc.close()
                    file = GraphWin("txtfile", 300, 150)
                    back = Button(file, "yellow", "back", Point(250, 30), 20)
                    showfile = Button(file, "red", "detail", Point(80, 80), 40)
                    readfile = Button(file, "white", "summary", Point(200, 80), 40)
                    m2 = file.getMouse()
                    
            if readfile.isClicked(m2):
                file.close()
                tc1 = GraphWin("Tutorial", 250, 250)
                back4 = Button(tc1, "green", "back", Point(175, 200), 20)
                ptext1 = Text(Point(120, 70), Tuto)
                ptext1.draw(tc1)
                m5 = tc1.getMouse()
                if back4.isClicked(m5):
                    tc1.close()
                    file = GraphWin("txtfile", 300, 150)
                    back = Button(file, "yellow", "back", Point(250, 30), 20)
                    showfile = Button(file, "red", "detail", Point(80, 80), 40)
                    readfile = Button(file, "white", "summary", Point(200, 80), 40)
                    m2 = file.getMouse()
                
            if back.isClicked(m2):
                file.close()
                win = GraphWin("School Event", 800, 500)
                background = Image(Point(400,250), "background.gif")
                background.draw(win)
                tutorial = Button(win, "white", "Tutorial", Point(400, 100), 85)
                community = Button(win, "white", "Community Meeting", Point(400, 250), 85)
                flex = Button(win, "white", "FLEX", Point(400, 400), 85)
                m = win.getMouse()
            
                    
        
        if community.isClicked(m):#user choose to see either flex or community meeting event
            win.close()
            file2 = GraphWin("Community Meeting", 300, 150)
            back2 = Button(file2, "yellow", "back", Point(250, 30), 20)
            showfile2 = Button(file2, "red", "detail", Point(80, 80), 40)
            readfile3 = Button(file2, "white", "summary", Point(200, 80), 40)
            m3 = file2.getMouse()
            if readfile3.isClicked(m3):
                file2.close()
                tc2 = GraphWin("Community Meeting", 300, 150)
                back5 = Button(tc2, "blue", "back", Point(175, 130), 20)
                ptext2 = Text(Point(150, 70), CM)
                ptext2.draw(tc2)
                m6 = tc2.getMouse()
                if back5.isClicked(m6):
                    tc2.close()
                    file2 = GraphWin("Community Meeting", 300, 150)
                    back2 = Button(file2, "yellow", "back", Point(250, 30), 20)
                    showfile2 = Button(file2, "red", "detail", Point(80, 80), 40)
                    readfile3 = Button(file2, "white", "summary", Point(200, 80), 40)
                    m3 = file2.getMouse()

            if showfile2.isClicked(m3):
                file2.close()
                tc3 = GraphWin("Here is the Friday Flash for Monday", 1000, 750)
                back9 = Button(tc3, "green", "back", Point(480, 100), 20)
                f3 = open("Event.txt", "r")
                content3 = f3.read()
                ptext3 = Text(Point(500, 350), content3)
                ptext3.draw(tc3)
                m7 = tc3.getMouse()
                if back9.isClicked(m7):
                    tc3.close()
                    file2 = GraphWin("Community Meeting", 300, 150)
                    back2 = Button(file2, "yellow", "back", Point(250, 30), 20)
                    showfile2 = Button(file2, "red", "detail", Point(80, 80), 40)
                    readfile3 = Button(file2, "white", "summary", Point(200, 80), 40)
                    m3 = file2.getMouse()
                    
            if back2.isClicked(m3):
                file2.close()
                win = GraphWin("School Event", 800, 500)
                background = Image(Point(400,250), "background.gif")
                background.draw(win)
                tutorial = Button(win, "white", "Tutorial", Point(400, 100), 85)
                community = Button(win, "white", "Community Meeting", Point(400, 250), 85)
                flex = Button(win, "white", "FLEX", Point(400, 400), 85)
                m = win.getMouse()
                
        if flex.isClicked(m):
            win.close()
            file0 = GraphWin("FLEX", 300, 150)
            back0 = Button(file0, "yellow", "back", Point(250, 30), 20)
            showfile0 = Button(file0, "red", "detail", Point(80, 80), 40)
            readfile0 = Button(file0, "white", "summary", Point(200, 80), 40)
            m3 = file0.getMouse()
            if readfile0.isClicked(m3):
                file0.close()
                tc3 = GraphWin("Flex schedule", 500, 300)
                back10 = Button(tc3, "yellow", "back", Point(250, 280), 20)
                ptext3 = Text(Point(250, 150), Flex)
                ptext3.draw(tc3)
                m9 = tc3.getMouse()
                if back10.isClicked(m9):
                    tc3.close()
                    file0 = GraphWin("txtfile", 300, 150)
                    back0 = Button(file0, "yellow", "back", Point(250, 30), 20)
                    showfile0 = Button(file0, "red", "detail", Point(80, 80), 40)
                    readfile0 = Button(file0, "white", "summary", Point(200, 80), 40)
                    m3 = file0.getMouse()
            if showfile0.isClicked(m3):
                file0.close()
                tc3 = GraphWin("Here is the Friday Flash for Monday", 1000, 250)
                f2 = open("Event.txt", "r")
                content2 = f2.read()
                back9 = Button(tc3, "yellow", "back", Point(500, 230), 20)
                ptext2 = Text(Point(500, 100), content2)
                ptext2.draw(tc3)
                m8 = tc3.getMouse()
                if back9.isClicked(m8):
                    tc3.close()
                    file0 = GraphWin("txtfile", 300, 150)
                    back0 = Button(file0, "yellow", "back", Point(250, 30), 20)
                    showfile0 = Button(file0, "red", "detail", Point(80, 80), 40)
                    readfile0 = Button(file0, "white", "summary", Point(200, 80), 40)
                    m3 = file0.getMouse()
            if back0.isClicked(m3):
                file0.close()
                win = GraphWin("School Event", 800, 500)
                background = Image(Point(400,250), "background.gif")
                background.draw(win)
                tutorial = Button(win, "white", "Tutorial", Point(400, 100), 85)
                community = Button(win, "white", "Community Meeting", Point(400, 250), 85)
                flex = Button(win, "white", "FLEX", Point(400, 400), 85)
                m = win.getMouse()
            


if __name__ == "__main__":
    main()
