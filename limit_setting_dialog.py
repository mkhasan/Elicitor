from tkinter import Tk, Canvas, Label, Frame, Button, Entry, LEFT, RIGHT, TOP, BOTTOM, N, S, E, W, StringVar, CENTER 
import tkinter as tk
from tkinter import ttk
from enum import Enum
#from tkinter.messagebox import showinfo


#block no starts from 1...block no 0 means spooler

class Attrib(Enum):
    CURRENT=1
    SPEED=2
    TORQUE=3
    POWER=4
    DENSER_POSITION=5
    DENSER_PRESSURE=6
    WIRE_TEMP=7
    DRUM_TEMP=8
    DICE_TEMP=9
    
    


def popup_bonus():
        win = tk.Toplevel()
        win.wm_title("Window")
        win.geometry("400x300")
        win.grab_set()
        
        l = tk.Label(win, text="Input")
        l.grid(row=0, column=0)
    
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)

class LimitSettingDlg():
    
    #@msgText1 = StringVar()
    #newLower = StringVar()
    def __init__(self, block_no, attrib, title, lower, upper, unit, coller):
        self.block_no = block_no
        self.attrib = attrib
        self.title = title
        self.unit = unit
        self.lower = lower
        self.upper = upper
        self.coller = coller
        
        self.newLower = StringVar()
        self.newLower.set("%.2f" % lower)
        self.newUpper = StringVar()
        self.newUpper.set("%.2f" % upper)
        
        
        self.msgText = StringVar()
        self.CreatePopUp()
        
        
    def OnSet(self):
        #self.win.grab_release()
        try:
            u = float(self.newLower.get())
            v = float(self.newUpper.get())
            
            print("%.2f and %.2f" % (u,v))
            if u >= v:
                              
                self.msgText.set("Lower must be less than Upper")        
               
            else:
                self.lower = u
                self.upper = v
                self.coller.OnDlgOkay(self.block_no, self.attrib, self.lower, self.upper)
                self.win.destroy()
            return    
        except Exception:
            self.msgText.set("Format error !!!")

        
     

    def CreatePopUp(self):
        if self.block_no == 0:
            blockStr = "Spooler"
        else:
            blockStr = "Block %d" % self.block_no
                 
        self.win = tk.Toplevel()
        self.win.wm_title("Set limits of %s" % blockStr)
        self.win.geometry("300x200")
        self.win.grab_set()
        
        form = Frame(self.win)
        form.pack(side=TOP, pady=(40,0), anchor=CENTER)
        
        Label(form, text="%s: " % self.title).grid()
        
        Label(form, text="Lower Value: ").grid(row=1, column=1)
        
        vcmd = (self.win.register(self.isOkay),'%P')
        Entry(form, validate="key", width=6, validatecommand=vcmd, textvariable=self.newLower, justify=RIGHT).grid(row=1, column=2)
        
        Label(form, text=" %s" % self.unit).grid(row=1, column=3)
        
        Label(form, text="Upper Value: ").grid(row=2, column=1)
        
        
        Entry(form, validate="key", width=6, validatecommand=vcmd, textvariable=self.newUpper, justify=RIGHT).grid(row=2, column=2)
        Label(form, text=" %s" % self.unit).grid(row=2, column=3)
        
        Button(self.win, text="Set", command=self.OnSet).pack(anchor=CENTER, pady=(30,0))
        
        
        self.msg = Label(self.win, textvariable=self.msgText, fg="red")
        self.msgText.set("")
        self.msg.pack()
        

    def isOkay(self, P):
        self.msgText.set("")
        print("got it")
        if len(P) == 0:
            return True
        
        t = int(1.2)
        print(t)
        try:
            val = float(P)
            s = P.split(".")
            if len(s) > 1 and len(s[1])>2:
                return False 
        except Exception:
            return False
            
        return True
        """
        print("%s %s %s" % (why, where, what))
        if (what >= '0' and what <='9' or what = ) :
            return False
        return True
           """ 
        """
        l = tk.Label(self.win, text="Input")
        l.grid(row=0, column=0)
    
        b = ttk.Button(self.win, text="Okay", command=self.OnOkay)
        b.grid(row=1, column=0)
        """
        
    
   
    def onclick(self):
        self.Quit()
        
    
class Application(Frame):
    
    lower = 0
    upper = 1

    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master
        self.pack()
        self.btn = Button(master, text="Click Me", command=self.onclick)
        self.btn.pack()
        
        self.onUpdate()
    
    
    def onUpdate(self):
        print("lower %d and upper %d", (self.lower, self.upper))    
        #self.after(2000, self.onUpdate)        
        
                     
    def Clicked(self):
        print("clicked")
        
    def onclick(self):
        LimitSettingDlg(block_no=1, attrib=Attrib.CURRENT, title="Current", lower=5.1, upper=10.00, unit="amp", coller = self)
    
        
    def OnDlgOkay(self, block_no, attrib, lower, upper):
        #print("test %d %d" % (self.dlg.lower, self.dlg.upper))
        
        try:
            self.lower = float(lower)
        except Exception:
            pass
        
        print("block no %d, attrib %s, lower %.2f, upper %.2f" % (block_no, attrib, self.lower, upper))
        

    


def key(event):
    print ("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        root.quit()



root = Tk()

if __name__ == '__main__':
    
    root.geometry("640x480")
    root.title("Elicitor")
    
    root.bind("<Key>", key)
    
    Application(root)    
    
    root.mainloop()


