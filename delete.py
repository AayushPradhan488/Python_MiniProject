from time import sleep
import tkinter as tk
from itertools import combinations
from math import *
from PIL import ImageGrab
import win32gui

print("Started!")

global root
capture_no=0
k=250
win=(50,50,450,450)

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

def destroy_object(i):
    global list_of_objects,gravitylist,objlist
    list_of_objects.remove(i)
    objlist.remove(i)
    gravitylist=list(combinations(list_of_objects,2))
    print("Gravitylist=",len(gravitylist),"\tList Of Objects=",len(list_of_objects))

def getter(widget):
    global capture_no
    '''x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("images\\{}.jpg".format(capture_no))
    capture_no+=1'''

    HWND = canvas.winfo_id()  # get the handle of the canvas
    rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
    ImageGrab.grab(rect).save("images\\{}.jpg".format(capture_no))
    capture_no+=1

    print("Image captured!")

def snapCanvas(canvas):
    global capture_no
    print('\n def _snapCanvas(self):')
    c = (canvas.winfo_rootx(),canvas.winfo_rooty(),canvas.winfo_rootx()+500,canvas.winfo_rooty()+500)
    grabcanvas = ImageGrab.grab(bbox=c)
    grabcanvas.save("images\\{}.jpg".format(capture_no))
    capture_no+=1

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

#canvas.create_line(250,0,250,500,fill='black')
#canvas.create_line(0,250,500,250,fill='black')
canvas.create_line(win[0],0,win[0],500,fill='black')
canvas.create_line(win[2],0,win[2],500,fill='black')
canvas.create_line(0,win[1],500,win[1],fill='black')
canvas.create_line(0,win[3],500,win[3],fill='black')

'''a=Ball(canvas,250,200,0,0)
b=Ball(canvas,150,100,0,0)
c=Ball(canvas,150,400,0,0)
d=Ball(canvas,250,300,0,0)
list_of_objects=[a,b,c,d]
gravitylist=list(combinations_with_replacement(list_of_objects,2))
#gravitylist=[(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]
objlist=[a,b,c,d]
root.update()
#sleep(2)'''

circular_placement_of_objects(100,250,200,40,canvas)
root.update()
sleep(2)
print("Gravitylist=",len(gravitylist),"\tList Of Objects=",len(list_of_objects))

cap=0
b=True
while b:
    '''if cap==10:
        snapCanvas(canvas)
        cap=0
    else:
        cap+=1'''
    gravity()
    for i in objlist:
        i.movex(i.vx)
        i.movey(i.vy)
        #a.movex(a.vx)
        #a.movey(a.vy)
        sleep(0.0001)
        if i.x>win[2]-i.vx or i.x<win[0]-i.vx or i.y>win[3]-i.vy or i.y<win[1]-i.vy:
            destroy_object(i)
        '''if i.x>win[2]-i.vx or i.x<win[0]-i.vx:
            i.vx= -i.vx
        if i.y>win[3]-i.vy or i.y<win[1]-i.vy:
            i.vy= -i.vy'''
        #if i.y>win[3]-i.vy or i.y<win[1]-i.vy: i.vy= -i.vy
        #    destroy_object(i)
    root.update()
    if len(objlist)==0:
        b=False

#tk.Label(root,text='hello').pack()

#tk.Button(canvas,text="Click Me!",command=callfunc).pack()
#callfunc()

#root.mainloop()

print("Success!")