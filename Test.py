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

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # all happends later in the def funtion.
        position = self.canvas.coords(self.id)  # creating a variable 'position' and calling out the function 'coords' and that function gives us back the cords of x y.Where our oval is in the window.
        if position[1] <= 0:#If position is <= 0 and if the ball hits the top of the screen the ball will stop moving out of our screen
            self.y = 1
            canvas.create_text(150, 300, text="Up")
        if position[3] >= self.canvas_height: #Checking if position is >= canvas.height (y) up and down.
            self.y = -1
            canvas.create_text(200, 300, text="Down")
        if position[0] <= 0:
            self.x = 3
            canvas.create_text(300, 100, text="Left")
        if position[2] >= self.canvas_width:#Checking if positon is >= canvas.with (x) left and right.
            self.x = -3
            canvas.create_text(250, 300, text="Right")
        # print(self.canvas.coords(self.id)) ___________ #Prints out our cords of the ball.




ball = Ball(canvas, 'red')#ball and color
while 1:#Main loop, contorls most of the program
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)#Change the speed of the ball.