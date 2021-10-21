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
    def __init__(self,canvas,kolor):#function init "__" = magic function (change behavor of function).
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill=kolor)#reading function canvas.create.oval and their parameters.
        self.canvas.move(self.id, 245,100)#We are moving the oval to the center of the canvas.
    def draw(self):
        self.canvas.move(self.id,0,-1)#All happends canvas -1 = move 1 px on the screen up.

ball = Ball(canvas, 'red')
while 1:#Main loop, contorls most of the program
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)