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

class Ball:#Class created called ball
    def __init__(self,canvas,color):#function init "__" = magic function (change behavor of function).
        self.canvas = canvas
        self.id =  canvas.create_rectangle(100,100,100,100, fill=color)#reading function canvas.create.oval and their parameters.
        self.canvas.move(self.id, 30,300)#We are moving the oval to the center of the canvas.
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)#all happends later in the def
        position = self.canvas.coords(self.id)#creating a variable 'position' and calling out the function 'coords'
        # and that function gives us back the cords of x y.Where our oval is in the window.
    if position[1] <= 0:
        self.y = 1
    if position[3] >= self.canvas.height:
        self.y = -1

ball = Ball(canvas, 'red')
while 1:#Main loop, contorls most of the program
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

