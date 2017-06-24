#!/bin/python3
from tkinter import Tk, Text, BOTH, X, StringVar, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
import math

TITLE = "Experiment Information"
WIDTH = 600
HEIGHT = 250
FONT = "Helvetica"
FSIZE = 12

out1 = ""

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Titling & Packing
        self.parent.title(TITLE)
        self.pack(fill=BOTH, expand=True)
        # Centering Window
        halfw = self.parent.winfo_screenwidth()
        halfh = self.parent.winfo_screenheight()
        x = (halfw-WIDTH)/2
        y = (halfh-HEIGHT)/2
        self.parent.geometry("%dx%d+%d+%d" % (WIDTH,HEIGHT,x,y))

        # Preparing Variable
        self.entryVarName = StringVar()
        self.entryVarLength = StringVar()
        self.entryVarInterval = StringVar()
#        self.txtVar = StringVar()

        # Constructing Forms
        fr1 = Frame(self)
        fr1.pack(fill=X) 
        lableName = Label(fr1, text="Experiment Name", width=20, font=(FONT,FSIZE))
        lableName.pack(side=LEFT, padx=5, pady=5)
        entryName = Entry(fr1, textvariable = self.entryVarName,font=(FONT,FSIZE))
        entryName.bind("<Return>", self.onPressEnter)
        entryName.pack(fill=X, padx=5, pady=5, expand=True)
        
        fr2 = Frame(self)
        fr2.pack(fill=X)
        lableLength = Label(fr2, text="Time Length (hour)", width=20,font=(FONT,FSIZE))
        lableLength.pack(side=LEFT, padx=5, pady=5)
        entryLength = Entry(fr2, textvariable = self.entryVarLength,font=(FONT,FSIZE))
        entryLength.bind("<Return>", self.onPressEnter)
        entryLength.pack(fill=X, padx=5, pady=5, expand=True)

#        txt = Label(fr2, text="hii", textvariable = self.txtVar)
#       txt.pack(fill=BOTH, padx=5, pady=5, expand=True)

        fr3 = Frame(self)
        fr3.pack(fill=X)
        lableInterval = Label(fr3, text="Time Interval (sec)", width=20,font=(FONT,FSIZE))
        lableInterval.pack(side=LEFT, padx=5, pady=5)
        entryInterval = Entry(fr3, textvariable=self.entryVarInterval,font=(FONT,FSIZE))
        entryInterval.bind("<Return>",self.onPressEnter)
        entryInterval.pack(fill=X, padx=5, pady=5, expand=True)

        frBtn = Frame(self)
        frBtn.pack(fill=BOTH,expand=True)
        btn = Button(frBtn, text="Confirm", command=self.onButtonClick)
        btn.pack(fill=BOTH, padx=5, pady=5, expand=True)
        
    # Defining Event Methods
    def onButtonClick(self):
        exp_name = self.entryVarName.get()
        timeLengthHour = float(self.entryVarLength.get())
        timeStepSec = int(self.entryVarInterval.get())
        timeLength_sec = int(timeLengthHour*3600)
        imgNum = math.ceil(timeLength_sec / timeStepSec)
        print("IMGNUM="+str(imgNum))
        print("EXP_NAME="+exp_name)
        print("TIMELENGTH="+str(timeLength_sec))
        print("TIMESTEP="+str(timeStepSec))
        #print("EXP_NAME="+self.entryVarName.get())
        #print("TIMELENGTH"+self.entryVarLength.get()+" hours")
        #print("Time Interval: "+self.entryVarInterval.get()+ " seconds")
        #self.txtVar.set("Input: " + out1 )
        self.quit()

    def onPressEnter(self,event):
        self.onButtonClick()


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

#print("What I've got: " + out1)

