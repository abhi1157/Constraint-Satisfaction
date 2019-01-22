'''

ABHINAV GUPTA
2015B4A70602P

'''
import Tkinter as tk  # nope, Python 2

class Level:
    def __init__(self, na, h, w):
        self.na = na
        self.h = h
        self.w = w
        self.Blocks = implemen(h, w)

    class Block:
        def __init__(self, x, y,vib):
            self.x = x
            self.y = y
            self.vib=vib

def new(na, h, w):
    level = Level(na, h, w)
    return level

def implemen(h, w):
    Blocks = [[Level.Block(x, y,"green") for x in range(w)] for y in range(h)]
    return Blocks

def GUI(n,matrix):
    #n=4
    test1 = new("test", n, n)
    count=0
    for x in range(n):
        for y in range(n):
            if count%2==0:
                test1.Blocks[x][y].vib = "green"
            else:
                test1.Blocks[x][y].vib = "yellow"
            count=count+1
        if(n%2==0):
            count=count+1

    MagicSquare = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            MagicSquare[x][y] = test1.Blocks[x][y].vib

    w,h = 120*n, 120*n
    root = tk.Tk()
    root.title("Magic Square")
    frame = tk.Frame()
    frame.pack()
    canvas = tk.Canvas(frame, width=w, height=h)
    rows, cols = len(MagicSquare), len(MagicSquare[0])
    lis=matrix
    rw, rh = w // rows, h // cols
    jo=0
    for y, row in enumerate(MagicSquare):
        jok=0
        for x,vib in enumerate(row):
            xl = x * rw
            yu = y * rh
            xr = (x+1)*rw-1
            yb = (y+1)*rh-1
            canvas.create_rectangle(xl, yu, xr, yb, fill=vib, width=20)
            canvas.create_text((xr-60,yb-60),text=lis[jo][jok],font=("monotype corsiva", 30))
            jok=jok+1
        jo=jo+1
    canvas.pack()
    root.mainloop()
