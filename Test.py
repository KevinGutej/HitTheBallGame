from tkinter import *
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)#The windows that has our canvas has to be our first thing we do(top most!).
canvas = Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)#No border around our canvas.
canvas.pack()
tk.update()


class Ball:#Class created called ball.
    def __init__(self,canvas,kolor):#function init "__" = magic function (change behavor of function).
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill=kolor)#reading function canvas.create.oval and their parameters.
        self.canvas.move(self.id, 245,100)#We are moving the oval to the center of the canvas.
        begin = [-3, -2, -1, 1, 2, 3]
        random.shuffle(begin)
        self.x = begin[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def random_rectangle(self,width, height):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        canvas.create_rectangle(x1, y1, x2, y2)

    def random_circle(self,width, height):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        canvas.create_oval(x1, y1, x2, y2)

    def random_squares(self,width):
        x1 = random.randrange(width)
        y1 = x1
        x2 = x1 + random.randrange(width)
        y2 = x2
        canvas.create_rectangle(x1, y1, x2, y2)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # all happends later in the def funtion.
        position = self.canvas.coords(self.id)  # creating a variable 'position' and calling out the function 'coords' and that function gives us back the cords of x y.Where our oval is in the window.
        if position[1] <= 0:#If position is <= 0 and if the ball hits the top of the screen the ball will stop moving out of our screen
            self.y = 1
            self.random_rectangle(500, 400)
        if position[3] >= self.canvas_height: #Checking if position is >= canvas.height (y) up and down.
            self.y = -1
            self.random_circle(500,400)

        if position[0] <= 0:
            self.x = 3
            self.random_squares(500)

        if position[2] >= self.canvas_width:#Checking if positon is >= canvas.with (x) left and right.
            self.x = -3

        # print(self.canvas.coords(self.id)) ___________ #Prints out our cords of the ball.




ball = Ball(canvas, 'red')#ball and color
while 1:#Main loop, contorls most of the program
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)#Change the speed of the ball.







from tkinter import *
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball:#Class created called ball.
    def __init__(self,canvas,paddle,kolor):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=kolor)
        self.canvas.move(self.id, 245,100)
        self.score = 0
        begin = [-3, -2, -1, 1, 2, 3]
        random.shuffle(begin)
        self.x = begin[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(position) == True:
            self.y = -3
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3



    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score += 1
                return True
        return False







class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>')

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)