import tkinter as tk
from itertools import combinations
from turtle import bgcolor, right
import pandas as pd

filepath = 'Data.xlsx'

G=10

data = pd.read_excel(filepath)
#print(data.iloc[1][0])

class Body:
    #x,y,m
    arr = [];v=500
    
    def __init__(self,canvas,x,y,m,vx,vy):
        self.x=x
        self.y=y
        self.m=m
        self.vx=vx
        self.vy=vy
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, fill="red")
    
    def display(arr):
        for i in arr:
            print("x=",i.x,"\ty=",i.y,"\tm=",i.m,"\tvx=",i.vx,"\tvy=",i.vy)
    
    def getData(canvas):
        for i in data.iterrows():
            x1 = i[1][0]
            y1 = i[1][1]
            m1 = i[1][2]
            vx1 = 0
            vy1 = 0
            newobj = Body(canvas,x1,y1,m1,vx1,vy1)
            Body.arr.append(newobj)
    
    def distance(x,y):
        return (x-y)**2
    
    def relate(self):
        for i in self.arr:
            rx=0 ; ry=0 ; ml=0 ; ax=0 ; ay=0
            for j in self.arr:
                if i!=j:
                    rx += (i.x-j.x)**2
                    ry += (i.y-j.y)**2
                    ml += j.m
                    print("Inin")
            if rx!=0:
                ax=(G*ml)/rx
            if ry!=0:
                ay=(G*ml)/ry
            i.vx+=ax*self.v
            i.vy+=ay*self.v
            Body.move_ball(self,i.vx,i.vy)
    
    def move_ball(self,vx,vy):
        self.canvas.move(self.ball, vx, vy)
        self.canvas.after(50, self.move_ball)

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")
    
    def move_ball(self,vx,vy):
        self.canvas.move(self.ball, vx, vy)
        self.canvas.after(50, self.move_ball)

#print(x,'\n',y,'\n',m)

def simFrame():
    root = tk.Tk()
    root.geometry('500x500')
    canvas = tk.Canvas(root,width=500,height=500)
    
    Body.getData(canvas)
    
    while True:
        Body.relate(Body)

#Body.getData()
#Body.display(Body.arr)
simFrame()

print("Success!")