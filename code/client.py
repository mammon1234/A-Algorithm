from Tkinter import *
import tkMessageBox
import ttk
import loadfile
import cell
import AstarPath
import printMap
import generateMap
import pathsave
import generateGoal
import mapSave
import time
import SequentialAstar
import IncrementalAstar

global MATRIX
global STARTROW
global STARTCOLUMN
global ENDROW
global ENDCOLUMN
global HARDCENTER
global path

class DorA:
    def __init__(self, parent):
        self.parent = parent
        self.combo()
    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value, state='readonly')
        self.box['values'] = ('1', '2','3','4','5')
        self.box.current(0)
        self.box.grid(row=1,column=5)

def generatemap():
    gm=generateMap.generateMap()

def loadFile():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    global HARDCENTER
    lf=loadfile.loadfile()
    (MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,HARDCENTER)=lf.getValue()
    print MATRIX
    lf.printM()

def certaincell():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN

    d1=v1.get()
    d2=v2.get()
    pstring= '['+d1+'] ['+d2+']'
    pstring = pstring+" Hvalue:"+str(MATRIX[int(d1)-1][int(d2)-1].getHvalue())+" Gvalue:"+str(MATRIX[int(d1)-1][int(d2)-1].getGvalue())
    pstring = pstring +" Fvalue:"+str(MATRIX[int(d1)-1][int(d2)-1].getFvalue())
    tkMessageBox.showinfo("Python command", pstring)

def generategoal():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    gg = generateGoal.generateGoal(MATRIX)
    (STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN)=gg.generate()
    print str(STARTROW)+"[]"+str(STARTCOLUMN)
    print str(ENDROW)+"[]"+str(ENDCOLUMN)
    # parent result should be reset



def findpath():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    global path
    path=set()
    path.clear()

    print str(STARTROW)+"[]"+str(STARTCOLUMN)
    print str(ENDROW)+"[]"+str(ENDCOLUMN)

    weight=v3.get()
    htype=dora.box_value.get()
    fp = AstarPath.AstarPath(MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,weight,htype)
    #print "finds"
    tim1=time.time()
    (MATRIX,path,len_path,len_expand)=fp.finding()
    tim2=time.time()
    print float(tim2-tim1)
    f = open('ans.txt', 'a+')
    f.write("("+str(STARTROW)+","+str(STARTCOLUMN)+")("+str(ENDROW)+","+str(ENDCOLUMN)+")")
    f.write(":"+str(weight)+":"+str(htype) + ":"+str(MATRIX[ENDROW][ENDCOLUMN].getGvalue())+":"+str(len_path)+":"+str(len_expand)+":"+str(tim2-tim1))
    f.write("\r\n")
    f.close()

def findSpath():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    global path
    path=set()
    path.clear()

    print str(STARTROW)+"[]"+str(STARTCOLUMN)
    print str(ENDROW)+"[]"+str(ENDCOLUMN)

    weight1=v3.get()
    weight2=v4.get()
    fp = SequentialAstar.SequentialAstar(MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,weight1,weight2)
    #print "finds"
    tim1=time.time()
    (MATRIX,path,len_path,len_expand)=fp.finding()
    tim2=time.time()
    print float(tim2-tim1)
    f = open('ans.txt', 'a+')
    f.write("("+str(STARTROW)+","+str(STARTCOLUMN)+")("+str(ENDROW)+","+str(ENDCOLUMN)+")")
    f.write(":"+str(weight1)+":"+str(weight2) + ":"+str(MATRIX[ENDROW][ENDCOLUMN].getGvalue())+":"+str(len_path)+":"+str(len_expand)+":"+str(tim2-tim1))
    f.write("\r\n")
    f.close()

def findIpath():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    global path
    path=set()
    path.clear()

    print str(STARTROW)+"[]"+str(STARTCOLUMN)
    print str(ENDROW)+"[]"+str(ENDCOLUMN)

    weight1=v3.get()
    weight2=v4.get()
    fp = IncrementalAstar.IncrementalAstar(MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,weight1,weight2)
    #print "finds"
    tim1=time.time()
    (MATRIX,path,len_path,len_expand)=fp.finding()
    tim2=time.time()
    print float(tim2-tim1)
    f = open('ans.txt', 'a+')
    f.write("("+str(STARTROW)+","+str(STARTCOLUMN)+")("+str(ENDROW)+","+str(ENDCOLUMN)+")")
    f.write(":"+str(weight1)+":"+str(weight2) + ":"+str(MATRIX[ENDROW][ENDCOLUMN].getGvalue())+":"+str(len_path)+":"+str(len_expand)+":"+str(tim2-tim1))
    f.write("\r\n")
    f.close()

def printmap():
    global MATRIX
    global path
    pm=printMap.printMap(MATRIX,path)
    pm.printM()

def pathSave():
    global MATRIX
    global ENDROW
    global ENDCOLUMN
    ps=pathsave.pathsave(MATRIX,ENDROW,ENDCOLUMN)
    ps.savefile()

def mapsave():
    global MATRIX
    global STARTROW
    global STARTCOLUMN
    global ENDROW
    global ENDCOLUMN
    global HARDCENTER
    mp = mapSave.mapSave(MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,HARDCENTER)
    mp.save()

root = Tk()
root.title("A_star")

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v6 = StringVar()


Label(root, text="Rows(1-120)",
      bg="red", width=30, height=2,
      wraplength=80, justify="left").grid(row=0, column=0)
Entry(root, width=30, textvariable=v1).grid(row=0, column=1)
v1.set("0")

Label(root, text="Columns(1-160)",
      bg="red", width=30, height=2,
      wraplength=80, justify="left").grid(row=1, column=0)
Entry(root, width=30, textvariable=v2).grid(row=1, column=1)
v2.set("0")

Label(root, text="Weight",
      bg="red", width=30, height=2,
      wraplength=80, justify="left").grid(row=2, column=0)
Entry(root, width=30, textvariable=v3).grid(row=2, column=1)
v3.set("1")

Label(root, text="Weight2",
      bg="red", width=30, height=2,
      wraplength=80, justify="left").grid(row=3, column=0)
Entry(root, width=30, textvariable=v4).grid(row=3, column=1)
v4.set("2")

dora=DorA(root)

Button(root, text="GenerateMap", fg="blue", bd=2, width=28, command=generatemap).grid(row=4,column=0)
Button(root, text="LoadFile", fg="blue", bd=2, width=28, command=loadFile).grid(row=4,column=1)
Button(root, text="Certain Cell", fg="blue", bd=2, width=28, command=certaincell).grid(row=4,column=2)
Button(root, text="Generate New Goal", fg="blue", bd=2, width=28, command=generategoal).grid(row=4,column=3)
Button(root, text="Save Map", fg="blue", bd=2, width=28, command=mapsave).grid(row=5,column=0)
Button(root, text="Print Path", fg="blue", bd=2, width=28, command=printmap).grid(row=5,column=1)
Button(root, text="Save Path", fg="blue", bd=2, width=28, command=pathSave).grid(row=5,column=2)
Button(root, text="Reset Matrix and Find Path", fg="blue", bd=2, width=28, command=findpath).grid(row=5,column=3)
Button(root, text="Sequential Astar and Find Path", fg="blue", bd=2, width=28, command=findSpath).grid(row=6,column=0)
Button(root, text="Incremental Astar and Find Path", fg="blue", bd=2, width=28, command=findIpath).grid(row=6,column=1)


root.mainloop()
