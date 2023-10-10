#Code by Aayush Pradhan
#N-Body Simulation

#Importing necessary modules
from time import sleep
import tkinter as tk
from itertools import combinations
from math import *
#from PIL import ImageGrab
#import win32gui

#Defining Number of Bodies and radius of circular placement
N_obj = 20
radius = 40

print("Started!")

#Defining global parameters
global root
#capture_no=0
k=250
win=(50,50,450,450)

#func for finding distance between 2 bodies
def dist(a,b):
    rx = pow(a.x - b.x,2)
    ry = pow(a.y - b.y,2)
    if rx>0.5:
        rx=(k)/rx
    else:
        rx=0
    if ry>0.5:
        ry=(k)/ry
    else:
        ry=0
    return rx,ry

#Gravitational force calculator
def gravity():
    global gravitylist
    for i in gravitylist:
        vx,vy=dist(i[0],i[1])
        if pow(vx+vy,0.5) < 1:
            if i[0].x-i[1].x >0:
                i[0].vx+=-vx
                i[1].vx+=vx
            else:
                i[0].vx+=vx
                i[1].vx+=-vx
            if i[0].y-i[1].y >0:
                i[0].vy+=-vy
                i[1].vy+=vy
            else:
                i[0].vy+=vy
                i[1].vy+=-vy

#func for placing N-bodies in circular array
def circular_placement_of_objects(n,cx,cy,r,canvas):
    global gravitylist,objlist,list_of_objects
    theta=360/n
    alpha=0
    list_of_objects=[]
    for i in range(n):
        obj=Ball(canvas,cx+(r*cos(alpha+(i*theta))),cy+(r*(sin(alpha+(i*theta)))),0,0)
        list_of_objects.append(obj)
    gravitylist=list(combinations(list_of_objects,2))
    objlist=list_of_objects.copy()

#func for reducing number of bodies for optimizing calculation
def destroy_object(i):
    global list_of_objects,gravitylist,objlist
    list_of_objects.remove(i)
    objlist.remove(i)
    gravitylist=list(combinations(list_of_objects,2))
    print("Gravitylist=",len(gravitylist),"\tList Of Objects=",len(list_of_objects))

#class defining bodies
class Ball:
    def __init__(self,canvas,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.canvas=canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.obj=canvas.create_oval(x-5,y-5,x+5,y+5,fill='black')
        self.xinc=0
        self.yinc=0
    
    def movex(self,xinc):
        self.canvas.move(self.obj,xinc,0)
        self.x+=xinc
    
    def movey(self,yinc):
        self.canvas.move(self.obj,0,yinc)
        self.y+=yinc
        
root=tk.Tk()
root.title("Moving balls")
root.geometry('500x500')
root.resizable(False, False)

canvas = tk.Canvas(root,bg='blue',width=500,height=500)
canvas.pack()

canvas.create_line(win[0],0,win[0],500,fill='black')
canvas.create_line(win[2],0,win[2],500,fill='black')
canvas.create_line(0,win[1],500,win[1],fill='black')
canvas.create_line(0,win[3],500,win[3],fill='black')

circular_placement_of_objects(N_obj,250,200,radius,canvas)
root.update()
sleep(2)
print("Gravitylist=",len(gravitylist),"\tList Of Objects=",len(list_of_objects))

b=True
while b:
    gravity()
    for i in objlist:
        i.movex(i.vx)
        i.movey(i.vy)
        sleep(0.0001)
        if i.x>win[2]-i.vx or i.x<win[0]-i.vx or i.y>win[3]-i.vy or i.y<win[1]-i.vy:
            destroy_object(i)
    root.update()
    if len(objlist)==0:
        b=False

print("Success!")