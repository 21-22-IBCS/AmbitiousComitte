from graphics import*
from Button import*

def main():
 
    win = GraphWin("Image Editor", 800, 600)
    exchange = Button(win, "white", "USD exchange", Point(350, 50), 70)
    
    close = Button(win, "grey", "Close", Point(350, 560), 45)
    korea = Button(win, "white", "Korea", Point(720, 50), 45)
    europe = Button(win, "white", "Europe", Point(720, 150), 45)
    england = Button(win, "white", "England", Point(720, 250), 45)
    japan = Button(win, "white", "Japan", Point(720, 350), 45)
    china = Button(win, "white", "Korea", Point(720, 450), 45)
    vietnam = Button(win, "white", "Vietnam", Point(720, 550), 45)
 
    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if vietnam.isClicked(m):
            print("How much:")
            amount = input()
            vnd = int(amount) * 22716
            print(amount + " USD = " + f'{ vnd: ,}' + " vnd ")
        "if .isClicked(m):"
        "if sh.isClicked(m):"
        "if sh.isClicked(m):"
        "if sh.isClicked(m):"
        "if sh.isClicked(m):"
        m = win.getMouse()
 
    win.close()
   
if __name__ == "__main__":
    main()
 


print( "What currencies do you want to change to (china, vietnam, japan, europe, korea, england):")
country = input()

print("How much: ")
amount = input()

vnd = int(amount) * 22716
cny = int(amount) * 6.46 
jpy = int(amount) * 110.27
eur = int(amount) * 0.85
won = int(amount) * 1196.91
pound = int(amount) * 0.74
if country == "china":
    print(amount + " USD = " + f'{ cny: ,}' + " ¥ ")
elif country == "vietnam" :
    print(amount + " USD = " + f'{ vnd: ,}' + " vnd ")
elif country == "japan":
    print(amount + " USD= " + f'{jpy: ,}' + " yen ")
elif country == "europe":
    print(amount + " USD= " + f'{eur: ,}' + " euros ")
elif country == "korea" :
    print(amount + " USD = " + f'{ won: ,}' + " won ")
elif country == "england" :
    print(amount + " USD = " + f'{ won: ,}' + " pound sterling ") 
    





