import tkinter
import speech_recognition as sr
import threading
from tkinter import *
from time import sleep
from math import *
import sys
from PIL import Image,ImageTk
import os
def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Interpreting...")
        query = r.recognize_google(audio,language='en-IN')
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query
class Drawing :
    circles=[]
    circles.append(None)
    lines = []
    lines.append(None)
    rectangles=[]
    rectangles.append(None)
    ovals=[]
    ovals.append(None)
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x400')
        self.root.title("Canvas Drawing")
        self.root.resizable(width=False,height=False)
        self.root.config(background="beige")
    def run(self) :
        load = Image.open(r"C:\Users\user\OneDrive\Desktop\Final Project\Python files\axes.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=20, y=32,anchor=NW)
        self.canvas = Canvas(self.root,width=300,height=300,highlightthickness=1, highlightbackground="black",background='white')
        self.canvas.place(x=300,y=300)
        self.canvas.pack(pady=50,side="bottom",expand = False)
        self.root.bind()
        self.root.mainloop()
    def figures(self) : 
        fig ="" 
        while fig!="exit" :
            fig = takeCommand().split()
            print("In class", str(fig))
            try :
                if fig[0] == "circle" :
                    self.circles.append(self.canvas.create_oval( (int(fig[3])-int(fig[7])), (int(fig[5])+int(fig[7])),(int(fig[3])+int(fig[7])),(int(fig[5])-int(fig[7])),outline="black"))
                elif fig[0] == "line" :
                    self.lines.append(self.canvas.create_line(fig[4],fig[6],int(fig[4])+int(fig[2]),fig[6]))
                elif fig[0] == "rectangle" :
                    self.rectangles.append(self.canvas.create_rectangle(int(fig[7])-int(fig[2])/2,int(fig[9])-int(fig[4])/2,int(fig[7])+int(fig[2])/2,int(fig[9])+int(fig[4])/2))
                elif fig[0] == "delete" :
                    self.deleteFig(fig)
                elif fig[0] == "rotate" :
                    if len(fig)==5 :
                        self.rotateFig(fig[1],int(fig[2]),int(fig[3]))
                    else :
                        self.rotateFig(fig[1],int(fig[2]),None)
                elif fig[0] == "replace" :
                    self.move(fig[1],int(fig[2]),int(fig[4]),int(fig[6]))
                elif fig[0] == "colour" or fig[0] == "Colour":
                    self.Color(fig[1],int(self.numMap(fig[2])),fig[3])
                elif fig[0]=="exit" :
                    self.root.destroy()
                    return 0
            except Exception as e :
                print(e)
    def numMap(self,number) :
        switcher = {
            "zero" : 0,
            'one' : 1,
            'two' : 2,
            'three' :3,
            'four' : 4,
            'five' :5,
            'six' : 6,
            'seven' : 7,
            'eight':8,
            'nine':9,
            'ten' : 10,
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
        }
        return switcher.get(number,'invalid number')
    def deleteAll(self,name) :
        if name == 'circles' :
            for j in range(0,len(self.circles)) :
                self.canvas.delete(self.circles[j])
        if name == 'lines' :
            for j in range(0,len(self.lines)) :
                self.canvas.delete(self.lines[j])
        if name == 'rectangles' :
            for j in range(0,len(self.rectangles)) :
                self.canvas.delete(self.rectangles[j])
    def deleteFig(self,name) :
        print("In delete :  ",name[0],name[1],name[2])
        if name[1]!= "all" :
            i = int(self.numMap(name[2]))
            if name[1] == "circle" :
                self.canvas.delete(self.circles[i])
            elif name[1] == "line" :
                self.canvas.delete(self.lines[i])
            elif name[1] == "rectangle" :
                self.canvas.delete(self.rectangles[i])
        elif name[1]=="all" :
            self.deleteAll(name[2])
    def rotateFig(self,name,num,angle) :
        if name =="line" :
            pts=list(self.canvas.coords(self.lines[num]))
            midx,midy = (pts[0]+pts[2])/2,(pts[1]+pts[3])/2
            newx1 = (pts[0]-midx)*cos(radians(angle))-(pts[1]-midy)*sin(radians(angle))+midx
            newy1 = (pts[0]-midx)*sin(radians(angle))+(pts[1]-midy)*cos(radians(angle))+midy
            newx2 = (pts[2]-midx)*cos(radians(angle))-(pts[3]-midy)*sin(radians(angle))+midx
            newy2 = (pts[2]-midx)*sin(radians(angle))+(pts[3]-midy)*cos(radians(angle))+midy
            print(newx1,newy1,newx2,newy2)
            self.canvas.delete(self.lines[num])
            self.lines[num]=None
            self.lines[num] = (self.canvas.create_line(newx1,newy1,newx2,newy2))
        elif name =="rectangle" :
            pts=list(self.canvas.coords(self.rectangles[num]))
            print(pts)
            fillColor = self.canvas.itemcget(self.rectangles[num],"fill")
            midx,midy = (pts[0]+pts[2])/2,(pts[1]+pts[3])/2
            len,bre = abs(pts[0]-pts[2]),abs(pts[1]-pts[3])
            print(midx,midy,len,bre)
            self.canvas.delete(self.rectangles[num])
            self.rectangles[num] =self.canvas.create_rectangle(midx-(bre/2),midy-(len/2),midx+(bre/2),midy+(len/2),fill=fillColor)
    def move(self,name,num,x,y) :
        if name=="line" :
            pts=list(self.canvas.coords(self.lines[num]))
            print(pts)
            xdiff,ydiff = pts[0]-x,pts[1]-y
            newx1,newy1 = pts[0]-xdiff,pts[1]-ydiff
            newx2,newy2 = pts[2]-xdiff,pts[3]-ydiff
            print(newx1,newy1,newx2,newy2)
            self.canvas.delete(self.lines[num])
            self.lines[num] = None
            self.lines[num] = self.canvas.create_line(newx1,newy1,newx2,newy2)
        elif name == "rectangle" :
            fillColor = self.canvas.itemcget(self.rectangles[num],"fill")
            pts=list(self.canvas.coords(self.rectangles[num]))
            print(pts)
            xdiff,ydiff = pts[0]-x,pts[1]-y
            newx1,newy1 = pts[0]-xdiff,pts[1]-ydiff
            newx2,newy2 = pts[2]-xdiff,pts[3]-ydiff
            print(newx1,newy1,newx2,newy2)
            self.canvas.delete(self.rectangles[num])
            self.rectangles[num] = None
            self.rectangles[num] = self.canvas.create_rectangle(newx1,newy1,newx2,newy2,outline="black",fill=fillColor)
        elif name =="circle" :
            fillColor = self.canvas.itemcget(self.circles[num],"fill")
            pts=list(self.canvas.coords(self.circles[num]))
            print(pts)
            radius = (pts[2]-pts[0])/2
            self.canvas.delete(self.circles[num])
            self.circles[num] = None
            self.circles[num] = self.canvas.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),outline="black",fill=fillColor)
    def Color(self,name,num,color) :
        if name=="circle" :
            self.canvas.itemconfig(self.circles[num],fill=color)
        elif name=="rectangle" :
            self.canvas.itemconfig(self.rectangles[num],fill=color)
        elif name == "egg" :
            self.canvas.itemconfig(self.ovals[num],fill=color)
def OpenWindow() :
    comm=""
    x=Drawing()
    print("In main " + comm)
    thread1 = threading.Thread(target=x.figures)
    thread1.start()
    x.run()
    if thread1.is_alive()!=True :
        thread1.join()
    processid =os.getpid()
    os.system('TASKKILL /F /PID '+ str(processid))
    sys.exit("exited")
if __name__ == '__main__' :
    OpenWindow()
    

    
    


