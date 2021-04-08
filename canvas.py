import speech_recognition as sr
import threading
from tkinter import *
from time import sleep
from math import *

def takeCommand():
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in')
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return query

class Drawing :
    circles=[]
    lines = []
    rectangles=[]
    ovals=[]

    

    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x300')
        # self.draw()
    # def draw(self) :
        self.canvas = Canvas(self.root,width=300,height=300)
        self.canvas.pack(side="bottom",fill=BOTH,expand = False)
    
    def run(self) :
        self.root.mainloop()
        
    
    def figures(self) :  
        while True :
            fig = list(takeCommand().split(' '))
            print("In class", fig)
            try :
                if fig[0] == "circle" :
                    self.circles.append(self.canvas.create_oval( (int(fig[1])-int(fig[3])), (int(fig[2])+int(fig[3])),(int(fig[1])+int(fig[3])),(int(fig[2])-int(fig[3])),outline="black"))
                elif fig[0] == "line" :
                    self.lines.append(self.canvas.create_line(fig[1],fig[2],fig[3],fig[4]))
                elif fig[0] == "rectangle" :
                    self.rectangles.append(self.canvas.create_rectangle(fig[1],fig[2],fig[3],fig[4]))
                elif fig[0] == "ellipse" :
                    self.ovals.append(self.canvas.create_oval((int(fig[1])-int(fig[4])), (int(fig[2])+int(fig[3])),(int(fig[1])+int(fig[4])),(int(fig[2])-int(fig[3])),outline="black"))
                elif fig[0] == "delete" :
                    self.deleteFig(fig)
                elif fig[0] == "rotate" :
                    self.rotateFig(fig[1],int(fig[2]),int(fig[3]))
                elif fig[0] == "move" :
                    self.move(fig[1],int(fig[2]),int(fig[3]),int(fig[4]))

                elif fig[0]=="exit" :
                    return
            except Exception as e :
                print(e)
    
    def numMap(self,number) :
        switcher = {
            'zero' : 0,
            'one' : 1,
            'two' : 2,
            'three' :3,
            'four' : 4,
            'five' :5,
            'six' : 6,
            'seven' : 7,
            'eight':8,
            'nine':9,
            'ten' : 10
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
        if name == 'ovals' :
            for j in range(0,len(self.ovals)) :
                self.canvas.delete(self.ovals[j])

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
            elif name[1] == "oval" :
                self.canvas.delete(self.ovals[i])
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
            pts=list(self.canvas.coords(self.rectangles[num]))
            print(pts)
            xdiff,ydiff = pts[0]-x,pts[1]-y
            newx1,newy1 = pts[0]-xdiff,pts[1]-ydiff
            newx2,newy2 = pts[2]-xdiff,pts[3]-ydiff
            print(newx1,newy1,newx2,newy2)
            self.canvas.delete(self.rectangles[num])
            self.rectangles[num] = None
            self.rectangles[num] = self.canvas.create_rectangle(newx1,newy1,newx2,newy2)
        elif name =="circle" :
            pts=list(self.canvas.coords(self.circles[num]))
            print(pts)
            radius = (pts[2]-pts[0])/2
            self.canvas.delete(self.circles[num])
            self.circles[num] = None
            self.circles[num] = self.canvas.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),outline="black")
        elif name=="ellipse" :
            pts=list(self.canvas.coords(self.ovals[num]))
            print(pts)
            a,b = abs(pts[1]-pts[3])/2,abs(pts[0]-pts[2])/2
            self.canvas.delete(self.ovals[num])
            self.ovals[num] = None
            self.ovals[num] = self.canvas.create_oval(int(x-b),int(y-a),int(x+b),int(y+a),outline="black")
    
            
def canvasthread() :
    
    while True :
        comm = takeCommand()
        print("In main " + comm)
        if comm == "canvas" or comm == "Canvas" :
            
            x=Drawing()
            # thread = threading.Thread(target=x.draw)
            thread1 = threading.Thread(target=x.figures)
            
            # thread.start()
            
            # sleep(0.3)
            thread1.start()
            sleep(0.5)
            
           
            x.run()
            # thread.join()
            thread1.join()
           
        if comm == "exit" :
            break

if __name__ == '__main__' :
    canvasthread()

    


