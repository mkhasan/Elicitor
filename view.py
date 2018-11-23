


from tkinter import Tk, Frame, Canvas, Button, BOTH, Label, PhotoImage, \
    StringVar, OptionMenu, ttk, LEFT, RIGHT, TOP, BOTTOM, NW, NE, SW, SE, \
    SUNKEN, RAISED, FLAT, RIDGE, GROOVE, E, W, N, S, CENTER
        
from tkinter.font import Font        
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
    
from constants import *    

import time    
from lxml.isoschematron import _xml_schema_root
from xdg.Locale import expand_languages

from data_manager import *     
from _ast import If

import sys
#from tensorflow.python.training.checkpointable.data_structures import sticky_attribute_assignment
    
def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())        


root = Tk()



# second page




imageP = tk.PhotoImage(file="./image/progress.png")
imageQ = PhotoImage(file="./image/speed.png")
greenBall = PhotoImage(file='image/green.png')
yellowBall = PhotoImage(file='image/yellow.png')

redBall = PhotoImage(file='image/red.png')
class View:
    def __init__(self, root, dataManager):
        
        #ttk.Style().configure("TNotebook", padding=0, relief="ridge",)
        self.dataManager = dataManager
        
        
              
        
         
        
       
        style = ttk.Style()
        
        
        style.theme_create( "style1", parent="alt", settings={
#                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": BACKGROUNND  }},
                "TNotebook.Tab": {
                    "configure": {"padding": [5, 1], "background": "gray", "font": TAB_FONT},
                    "map":       {"background": [("selected", "white")],
                                  "expand": [("selected", [1, 1, 1, 0])] } },  
                "TFrame": {"configure": {"background": "white"}}} )
        
        
        

        style.theme_use("style1")
        
        
    
        gui_style = ttk.Style()
        
        gui_style.configure('Top.TFrame', background="white")
        gui_style.configure('Top.TNotebook', tabmargins=[2, 5, 2, 0], background=BACKGROUNND)
        #gui_style.configure('Top.TNotebook.Tab', tabmargins=[2, 5, 2, 0], background=BACKGROUNND)

        self.nb = ttk.Notebook(root, style='Top.TNotebook')
        
        
        

        self.page1 = Monitoring(self.nb, self.dataManager)#Page(self.nb)#Monitoring(root)
        # second page
        self.page2 = ttk.Frame(self.nb)  #Page(self.nb)
        
        
        
        
        self.page3 = ttk.Frame(self.nb)#Page(self.nb)
        
        self.page4 = ttk.Frame(self.nb)#Page(self.nb)
        
        self.page5 = ttk.Frame(self.nb)#Page(self.nb)
    
    
            
  
            
        
        self.nb.add(self.page1, text=MONITORING_TITLE)#, image=(image1, 'selected', imageP, '!disabled', imageQ))
        
        #ttk.Style().configure("TFrame", padding=10, relief="flat", background="blue")
        self.nb.add(self.page2, text=PLOT_TITLE)
        self.nb.add(self.page3, text=EDITOR_TITLE)
        self.nb.add(self.page4, text=INFORMATION_TITLE)
        self.nb.add(self.page5, text=SETTING_TITLE)
        
         
        
        
        self.nb.pack(padx=MONITORING_NB_PAD_X, expand=1, fill="both")
        
        
        
        
        #style.theme_use("style2")
        
        #Monitoring(self.page1, self.dataManager).pack(expand=1, fill="both", padx=0, pady=(40,0))
        #Canvas(self.page1, bg="red", bd=0, relief=FLAT, highlightthickness=0).pack(expand=1, fill="both")
        
        
        
shutdownImage = PhotoImage(file='image/shutdown.png')        
        
    
class Monitoring(ttk.Frame):
    
    def __init__(self, root, dataManager):
        ttk.Frame.__init__(self, root)
        #self.root = root
        self.dataManager = dataManager
        self.createWidgets()
        
    
    def createWidgets(self):

        #sidePanel = Frame(self, bg=SIDE_PANEL_BG)
        #sidePanel.pack(side=TOP, expand=1, fill="both", pady=(40,0) )
        #sidePanel.grid(row=0, column=0)
        
        
        
        
        processInfo = Frame(self)
        processInfo.pack(side=TOP, expand=1, fill="both", pady=(40,0), padx=(0,0), anchor=W)
        
        #processInfo.grid(padx=(0,100))
        
        #f1 = processInfo
        #f1=Frame(sidePanel, width=WINDOW_WIDTH-200, height=int(WINDOW_HEIGHT/2), bg="red")
        
        #f1.grid(row=0, column=0, columnspan=19)
        
        
        #sidePanel1.grid(row=0, column=19, sticky=NE)
        
        #self.AddToSidePanel(sidePanel1)
        
        
        
        
        
        wireInfo = Frame(processInfo, bg=RPOCESS_HEADER_BG)
        wireInfo.pack(side=LEFT, anchor=NW, padx=(20,0))
        
        Label(wireInfo, text=PROCESS_STR, font=(FONT_NAME_LARGE, FONT_SIZE_LARGE), bg="grey", width = INFO_TITLE_WIDTH, anchor=W, padx=10, pady=MONITORING_TITLE_PAD_Y, bd=0).pack(side=TOP)
        #Label(wireInfo, text="I.D.8", font=(FONT_NAME_LARGE, FONT_SIZE_LARGE),bg="grey", width = INFO_TITLE_WIDTH, anchor=W, padx=10, height=1, pady=0, bd=0 ).pack(side=TOP)
        
        
        ParamValue(wireInfo, 'Rod Pat Dia (mm)', '3.90')
        ParamValue(wireInfo, 'Input Wire Dia (mm)', '3.90')
        ParamValue(wireInfo, 'Output Wire Dia (mm)', '1.30')
        ParamValue(wireInfo, 'Material (Pat. Or)', '0.86')
        ParamValue(wireInfo, 'Taper', '27')
        ParamValue(wireInfo, 'Wire Speed (m/s)', '20.0')
        
        
        spoolerInfo = Frame(processInfo)
        spoolerInfo.pack(side=LEFT, anchor=NW, padx=(20, 0))

        
        
        
        tk.Label(spoolerInfo, text=SPOOLER_STR, font=(FONT_NAME_LARGE, FONT_SIZE_LARGE), bg=RPOCESS_HEADER_BG, width = INFO_TITLE_WIDTH, pady=MONITORING_TITLE_PAD_Y, anchor=W, padx=10, bd=0).pack(side=TOP)
        ParamValue(spoolerInfo, 'End Counter (M)', ' 1200')
        ParamValue(spoolerInfo, '속도(rmp)', '80')
        ParamValue(spoolerInfo, '트레바샤 폭(mm)', '700')
        ParamValue(spoolerInfo, 'M', '0.86')
        
        spoolerViewer = Frame(spoolerInfo, bg=SPOOLER_VIEW_BG)
        spoolerViewer.pack(anchor=W, pady=(50,0))
        

        #
        #my_canvas = tk.Canvas(spoolerViewer, bg='cyan', width=100, height=70)
        #my_canvas.pack()
        #ParamBar(spoolerViewer, 'Test')

        label1 = Label(spoolerViewer, text='전류 (A)', font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), bg=SPOOLER_VIEW_BG).grid(row=0, column=0, sticky=E, padx=(15,0))
        self.spoolerCurrent = SpoolerBar(spoolerViewer, 0, SPOOLER_VIEW_BG)
        self.spoolerCurrent.grid(row=0, column = 1, padx=30)
        

        Label(spoolerViewer, text='회전수 (rmp)', font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), bg=SPOOLER_VIEW_BG).grid(row=1, column=0, sticky=E, padx=(15,0))
        self.spoolerRPM = SpoolerBar(spoolerViewer, 0, SPOOLER_VIEW_BG)
        self.spoolerRPM.grid(row=1, column = 1, padx=30)
        
        Label(spoolerViewer, text='토크 (kgt/m)', font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), bg=SPOOLER_VIEW_BG).grid(row=2, column=0, sticky=E, padx=(15,0))
        self.spoolerTorque = SpoolerBar(spoolerViewer, 0, SPOOLER_VIEW_BG)
        self.spoolerTorque.grid(row=2, column = 1, padx=30)
        
        Label(spoolerViewer, text='줄력파워 (W)', font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), bg=SPOOLER_VIEW_BG).grid(row=3, column=0, sticky=E, padx=(15,0))
        self.spoolerPower = SpoolerBar(spoolerViewer, 0, SPOOLER_VIEW_BG)
        self.spoolerPower.grid(row=3, column = 1, padx=30)
        

        sidePanel = Frame(processInfo, bg=SIDE_PANEL_BG, width=SIDE_PANEL_WIDTH)
        sidePanel.pack(side=RIGHT, anchor=N, padx=(0,0), fill="y")
        
        self.AddToSidePanel(sidePanel)


        


        propertyViewer = Frame(processInfo)
        propertyViewer.pack(side=RIGHT, anchor=NE, padx=(0,20))
        
        
        #f1 = Frame(processInfo, width=100, height=100, bg="red")
        #f1.pack()
        utility = Frame(propertyViewer)
        utility.pack(anchor=E)
        Label(utility, text=UTILITY_STR, font=(FONT_NAME_LARGE, FONT_SIZE_LARGE), bg="grey", width = INFO_TITLE_WIDTH, pady=MONITORING_TITLE_PAD_Y, anchor=W, padx=10, bd=0).pack(side=TOP, anchor=E)      
        ParamValue(utility, '냉약수 (kgf/cm2)', '2.5')
        ParamValue(utility, '에어 압력 (kgf/cm2)', '4.32')
        ParamValue(utility, 's', '700')
        ParamValue(utility, 's', '0.86')
        
        image0 = PhotoImage(file="./image/progress.png")
        image1 = PhotoImage(file="./image/speed.png")

        self.SpeedAndCounterViewer(propertyViewer, '카운터', '정지', '현제', '54.321', '12.345', 'M', 'M', 0, image0)
        self.SpeedAndCounterViewer(propertyViewer, '선속 설정', '설정', '현제', '12.3', '12.5', 'm/s', 'm/s', (0,20), image1)
        
        #sidePanel1 = Frame(utility, width=SIDE_PANEL_WIDTH, bg="red")
        #sidePanel1.pack(side=TOP, anchor=E)
        
        #self.AddToSidePanel(sidePanel1)


        #f1 = Frame(self, bg="red")
        #f1.pack(expand=1, fill="both")
        
        self.motorInfo = MotorInfo(self, self.dataManager)
        
        self.motorInfo.pack(expand=1, fill="both")
        
        
            
        self.onUpdate()
    
    def Quit(self):
        print("testing123")
        #root.quit()
        
    def AddToSidePanel(self, sidePanel):
        alarmImage = PhotoImage(file='image/alarm.png')
        alarmLabel = Label(sidePanel, image=alarmImage, bd=0, width=SIDE_PANEL_WIDTH, bg=SIDE_PANEL_BG)
        alarmLabel.image = alarmImage
        alarmLabel.pack(pady=(40,0))

        warningImage = PhotoImage(file='image/warning.png')
        warningLabel = Label(sidePanel, image=warningImage, bd=0, width=SIDE_PANEL_WIDTH, bg=SIDE_PANEL_BG)
        warningLabel.image = warningImage
        warningLabel.pack(pady=(20,20))
        
        userImage = PhotoImage(file='image/user.png')
        userLabel = Label(sidePanel, image=userImage, bd=0, width=SIDE_PANEL_WIDTH, bg=SIDE_PANEL_BG)
        userLabel.image = userImage
        userLabel.pack(pady=(20,20))

        
        #shutdownImage = PhotoImage(file='image/shutdown.png')
        shutdownButton = Button(sidePanel, command=self.Quit)
        shutdownButton.config(image = shutdownImage)
        
        shutdownButton.pack(pady=(20,20))
        
        

        
    def SpeedAndCounterViewer(self, parent, title, param0, param1, value0, value1, unit0, unit1, padxValue, bottom_image):
        container = Frame(parent, bg='gray')
        #frame1.pack(side=RIGHT, anchor=S)
        container.pack(side=RIGHT, anchor=S, padx = padxValue, pady=(50,0) )
        Label(container, text=title, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), fg="red", bg=SPOOLER_VIEW_BG, width=5+6+3+4).pack(expand=1, fill="x")
        
        
        outer = Frame(container, bg='gray')
        outer.pack(side=TOP, anchor=CENTER)
        info = Frame(outer, bg='gray')
        info.pack(side=TOP, anchor=CENTER)
       
        
        Label(info, text=param0, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), fg=RPOCESS_INFO_VALUE_FG, bg='gray', anchor=W, width=5, bd=0).grid(row=0, column=0)
        
        Label(info, bd=2, relief=RIDGE, text=value0, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), width=6, anchor=CENTER, padx=0).grid(row=0, column=1, pady=10)
        
        Label(info, text=unit0, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), fg=RPOCESS_INFO_VALUE_FG, bg=RPOCESS_HEADER_BG, width=3, anchor=E, bd=0).grid(row=0, column=2, pady=0)
        
        Label(info, text=param1, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), fg=RPOCESS_INFO_VALUE_FG, bg=RPOCESS_HEADER_BG, width=5, anchor=W).grid(row=1, column=0, pady=10)
        
        Label(info, bd=2, relief=RIDGE, text=value1, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), width=6, anchor=CENTER, padx=0).grid(row=1, column=1, pady=10)
        
        Label(info, text=unit1, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), fg=RPOCESS_INFO_VALUE_FG, bg=RPOCESS_HEADER_BG, width=3, anchor=E, bd=0).grid(row=1, column=2, pady=10)
        
        
        
        bottom_image_label = Label(outer, image=bottom_image, bg='gray', width=200)
        bottom_image_label.image = bottom_image
        bottom_image_label.pack()

        #Label(container, text="Hello").pack()
        
        

    def onUpdate(self):
        
         
        
        spoolerData = self.dataManager.data.spoolerData
        
        #print("torque values are %s and %s" % (blockData[4].torque, blockData[6].torque))
        #self.realTimeDataTop.itemconfigure(self.denserText[3], text = "%.2f" % float(self.dataManager.val))
        indexCurrent = int(10.0*float(spoolerData.current/(MAX_CURRENT)))
        
        
        if indexCurrent > 9:
            indexCurrent = 9;
        
        indexRPM = int(10.0*float(spoolerData.rpm/(MAX_RPM)))
        if indexRPM > 9:
            indexRPM = 9
        
        indexTorque = int(10.0*float(spoolerData.current/(MAX_TORQUE)))
        if indexTorque > 9:
            indexTorque = 9;
                    
        self.spoolerCurrent.Draw(indexCurrent)
        self.spoolerRPM.Draw(indexRPM)
        self.spoolerTorque.Draw(indexTorque)
        self.spoolerPower.Draw(0)    

        self.motorInfo.onUpdate()
        self.after(1000, self.onUpdate)

class SpoolerBar(Canvas):

    def __init__(self, root, index, color):
        Canvas.__init__(self, root, bg=color, width=MONITORING_BAR_WIDTH, height=MONITORING_BAR_HEIGHT, bd=0, relief='ridge', highlightthickness=0)
        self.index = index
        self.Draw()
    def Draw(self, index=0):
        self.index=index
        gap = 2
        barWidth = int((MONITORING_BAR_WIDTH-8*gap)/9)
        
        
        color = [BAR_GREEN, BAR_YELLOW, BAR_RED]
        for k in range (index):
             
            x = barWidth/2 + (barWidth+gap)*k
            self.create_line(x, 0, x, MONITORING_BAR_HEIGHT, fill=color[int(k/3)], width=barWidth)
        

    
class ParamValue(Frame):
    def __init__(self, root, paramText, valueText):
        Frame.__init__(self, root)
        
        self.pack(side=TOP, expand=1, fill='x')
        Label(self, text=paramText, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL)).pack(side=LEFT)
        self.str = StringVar()
        Label(self, bd=2, relief=RIDGE, textvariable=self.str, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), width=8, anchor=E, padx=10, fg=RPOCESS_INFO_VALUE_FG).pack(side=RIGHT)
        self.str.set(valueText)
                
class ParamBar(Frame):
    def __init__(self, root, paramText):
        Frame.__init__(self, root, bg="blue")
        
        self.pack(side=TOP, expand=1, fill='x')
        Label(self, text=paramText, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), bg=SPOOLER_VIEW_BG).pack(side=LEFT)
        #self.str = StringVar()
        #Label(self, bd=2, relief=RIDGE, textvariable=self.str, font=(FONT_NAME_NORMAL, FONT_SIZE_NORMAL), width=8, anchor=E, padx=10).pack(side=RIGHT)
        #self.str.set(valueText)

            
class ProcessInfo(Frame):
    
    cnt = 0
    
    
    def __init__(self, root, color):
        Frame.__init__(self, root, relief=SUNKEN, bd=2)
        self.countStr = StringVar()
        self.createWidged()
        
    
    def createWidged(self):
        
        Frame.__init__(self, root, bg="grey")
        Label(self, text=PROCESS_STR, font=(FONT_NAME_LARGE, 24), bg="grey").pack(side=TOP)
        Label(self, text="I.D.8", font=(FONT_NAME_LARGE, 24),bg="grey" ).pack(side=BOTTOM, anchor=SW )
    
class MotorInfo(ttk.Notebook):
    
    cnt = 0
    
    motorStatus = []

    motorStatusText = []

    wireTempText = []
    denserText = []
    
    drumTempText = []
    diceTempText = []
    
    blockWidth = 0
    blockHeight = 0
    
    denserSignal = []
    wireTempSignal = []
    drumTempSignal = []
    diceTempSignal = []
    
    turn = 0
    
    def __init__(self, root, dataManager):
        #Frame.__init__(self, root, bg="blue")
        
        gui_style = ttk.Style()
        
    
        # in windows default background is #F0F0F0 but in linux it is #D9D9D9...However TNotebook for windows makes default notebook background as 
        # something no #FOFOFO...So we have to handle this separately    
        
        if sys.platform == "Windows":
            gui_style.configure('Bottom.TNotebook', tabmargins=[2, 5, 2, 0], background = "#F0F0F0")
        elif sys.platform == "linux":      
            gui_style.configure('Bottom.TNotebook', tabmargins=[2, 5, 2, 0], background = "#D9D9D9")

        
        
        ttk.Notebook.__init__(self, root, style='Bottom.TNotebook')
        
        
        self.pointAfterTab = self.GetPointAfterTab(gui_style)
            
        
        
        self.countStr = StringVar()
        
            
        
        self.root = root
        self.dataManager = dataManager
        self.createWidged()
        
    def GetPointAfterTab(self, s):
        tabmargins = s.lookup('Bottom.TNotebook', 'tabmargins')
        paddings = s.lookup('TNotebook.Tab', 'padding')
        
        font = s.lookup('TNotebook.Tab', 'font')
        
        #list = font.split(" ")
        point = 0
        
        point += (int(tabmargins[0])+int(tabmargins[2]))
        point += (2*int(paddings.split(" ")[0]))
        
        
        point += 2  # for focus
        
        list = TAB_FONT.split(" ")
        font = Font(family=list[0], size=int(list[1]))
        
        
        (w,h) = (font.measure(MOTOR_INFO_TEXT),font.metrics("linespace"))
        
        
        point += w
        
        
        return point
        
        
        
        
    def hello(self, event):
        print("hello")
    
    def onclick(self, event):
        cv = self.realTimeDataTop
        item = cv.find_closest(event.x, event.y)
        
        if self.turn == 0:
            cv.itemconfig(item, image=greenBall)
        else:
            cv.itemconfig(item, image=redBall)
            
        self.turn = 1-self.turn
        """
        current_color = cv.itemcget(item, 'fill')
    
        if current_color == 'black':
            cv.itemconfig(item, fill='white')
    
        else:
            cv.itemconfig(item, fill='black')
        """
        
        #cv.delete(item)

    def createWidged(self):
        
        
        denserValue = []
        wireTempValue = []
        
        
        for k in range(BLOCK_COUNT):
            denserValue.append(56.78)
            wireTempValue.append(56.78)
        
        

        #print("point after tab %d" % self.pointAfterTab)
        test= Canvas(self, width=SIDE_PANEL_WIDTH+0, height = 335+40, bd=1, highlightthickness=0, bg=SIDE_PANEL_BG)
        test.place(x=WINDOW_WIDTH-(MONITORING_NB_PAD_X*2), y=0, anchor=NE)
        
        test1= Canvas(self, width=WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)-self.pointAfterTab-2, height = 80, bd=1, highlightthickness=0, bg=SIDE_PANEL_BG)
        test1.place(x=self.pointAfterTab, y=23, anchor=NW)
    
       
        
        
        self.page1 = ttk.Frame(self)#Page(self.nb)
        
        
       
        
  
        self.add(self.page1, text="MOTOR INFORMATION")
        
        
        
        frame1 = Frame(self.page1, bg="white")
        frame1.pack(expand=1, fill="x", anchor=S)
        
        #titleFrame = Frame(self.page1, bg="red")
        #titleFrame.pack(side=LEFT, expand=1, fill="x")
        
        #Label(titleFrame, text="hello", width=5, anchor=E).pack(side=TOP, anchor=E)
        
        #barViewFrame = Frame(self.page1);
        #barViewFrame.pack(side=TOP, expand=1, fill="x", pady=(10,0))
        #frame1 = self.page1
        
        OFFSET = 2
        blockWidth = int((WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)+OFFSET)/14)       # OFFSET is used to make each bar_block little bigger than title frame
        self.blockWidth = blockWidth
        blockHeight = int((11*blockWidth)/10)
        self.blockHeight = blockHeight
         
        barViewCanvas = Canvas(frame1, height=blockHeight, bg="white", bd=0, highlightthickness=0)
        barViewCanvas.pack(expand=1, fill="x", pady=(0,0), anchor=N)
        
        self.barViewCanvas = barViewCanvas

        font = Font(family=FONT_NAME_SMALL, size=FONT_SIZE_SMALL)
        str = ["전류(A)", "회전수(rpm)", "토크(kgf/m)", "출력파워(W)", "댄서 위치(mm)"]
        
        (w,textHeight) = font.measure(str[0]),font.metrics("linespace")
        firstSeparator = WINDOW_WIDTH-(MONITORING_NB_PAD_X*2) - 13*blockWidth - 2
               
        
        
            #barViewCanvas.create_line(x, y, x+50, y, fill="gray", width=2 )
            
        
        x = firstSeparator
        # self.create_line(x, 0, x, BAR_CANVAS_HEIGHT, fill=color[int(k/3)], width=barWidth)
        for k in range(13):
            barViewCanvas.create_line(x, 0, x, blockHeight, fill=BLOCK_SEPARATOR, width=2 )    
            y = 0
            for l in range(5):
                y += int(blockHeight/6)
                if k==0:
                    barViewCanvas.create_text(x-5,y,fill="black",font=font, text=str[l], anchor=E)
                
                
            x += blockWidth
        """    
        for k in range(13):
            barViewCanvas.create_line(x, 0, x, blockHeight, fill=BLOCK_SEPARATOR, width=2 )    
            y = 0
            for l in range(5):
                y += int(blockHeight/6)
                if k==0:
                    barViewCanvas.create_text(x-5,y,fill="black",font=font, text=str[l], anchor=E)
                self.DrawBar(barViewCanvas, x, y, 9)
                
            x += blockWidth
            
        """    
        
        
        mechaPropertyCanvas = Canvas(frame1, height=blockHeight, bg=MECHA_VALUE_BG, bd=0, highlightthickness=0)
        mechaPropertyCanvas.pack(expand=1, fill="x")
        
        
        x = firstSeparator
        # self.create_line(x, 0, x, BAR_CANVAS_HEIGHT, fill=color[int(k/3)], width=barWidth)
        for k in range(13):
            mechaPropertyCanvas.create_line(x, 0, x, blockHeight, fill=BLOCK_SEPARATOR, width=2 )    
            x += blockWidth


        mechaTitleCanvas = Canvas(mechaPropertyCanvas, width=firstSeparator, height=blockHeight)
        mechaTitleCanvas.configure(bg=MECHA_TITLE_BG, bd=0, highlightthickness=0)
        mechaPropertyCanvas.create_window(0, 0, anchor=NW, window=mechaTitleCanvas)

        mechaTitleCanvas.create_line(firstSeparator, 0, firstSeparator, blockHeight, fill=BLOCK_SEPARATOR, width=2 )
        
        mechaTitleCanvas.create_line(0, 0, firstSeparator, 0, fill=BLOCK_SEPARATOR, width=4)
        mechaTitleCanvas.create_line(0, int(blockHeight/3), firstSeparator, int(blockHeight/3), fill=BLOCK_SEPARATOR, width=2)
        mechaTitleCanvas.create_line(0, int(2*blockHeight/3), firstSeparator, int(2*blockHeight/3), fill=BLOCK_SEPARATOR, width=2)
        mechaTitleCanvas.create_line(0, blockHeight, firstSeparator, blockHeight, fill=BLOCK_SEPARATOR, width=4)
        
        mechaPropertyCanvas.create_line(firstSeparator, 0, WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)-5, 0, fill=BLOCK_SEPARATOR, width=4)
        mechaPropertyCanvas.create_line(firstSeparator, int(blockHeight/3), WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)-5, int(blockHeight/3), fill=BLOCK_SEPARATOR, width=2)
        mechaPropertyCanvas.create_line(firstSeparator, int(2*blockHeight/3), WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)-5, int(2*blockHeight/3), fill=BLOCK_SEPARATOR, width=2)
        mechaPropertyCanvas.create_line(firstSeparator, blockHeight, WINDOW_WIDTH-(MONITORING_NB_PAD_X*2)-5, blockHeight, fill=BLOCK_SEPARATOR, width=4)

        title = ["다이스 직경 (mm)", "단면 감면율 (%)", "선속도 (m/s)"]
            
        x = int(firstSeparator/2)
        y =  int(blockHeight/6)
                
        for k in range(3):
            mechaTitleCanvas.create_text(x,y,fill="black",font=font, text=title[k], anchor=CENTER)
            y += int(blockHeight/3)
            
            
        mechaValue= [ [3.90, 3.44, 3.06, 2.73, 2.44, 2.20, 1.99, 1.81, 1.65, 1.52, 1.40, 1.30, 1.30]
                     ,[22.0, 21.2, 20.5, 19.7, 18.9, 18.1, 17.3, 16.5, 15.7, 14.8, 14.0, 14.0, 14.0]
                     ,[2.22, 2.28, 3.62, 4.55, 5,67, 6,99, 8.53, 10.32, 12,35, 14,65, 17.20, 20.00, 20.00]]  
        
        
        y =  int(blockHeight/6)
        for i in range(3):
            x = firstSeparator+int(blockWidth/2)
            for j in range(13):
                if i == 1:
                    mechaPropertyCanvas.create_text(x,y,fill="white",font=(FONT_NAME_SMALL, FONT_SIZE_SMALL, "bold"), text="%.1f" % mechaValue[i][j], anchor=W)
                else:
                    mechaPropertyCanvas.create_text(x,y,fill="white",font=(FONT_NAME_SMALL, FONT_SIZE_SMALL, "bold"), text="%.2f" % mechaValue[i][j], anchor=W)
                x += blockWidth
            
            y += int(blockHeight/3)     
        
    
        rowHeight = int(blockHeight/5)+5
        
        self.realTimeDataTop = Canvas(frame1, height=rowHeight*3, bg=REAL_TIME_DATA_BG, bd=0, highlightthickness=0)
        self.realTimeDataTop.pack(expand=1, fill="x")
        
        
        

        
        
        # top bar cotains denser and wire temperature  values
        x = firstSeparator
        y = 5
        # self.create_line(x, 0, x, BAR_CANVAS_HEIGHT, fill=color[int(k/3)], width=barWidth)
        for k in range(13):
            self.realTimeDataTop.create_line(x, 0, x, blockHeight, fill=BLOCK_SEPARATOR, width=2 )
            
            window = Canvas(self.realTimeDataTop, width=int(blockWidth/3), height=int(2*rowHeight/3))
            window.configure(bg=REAL_TIME_PRO_TITLE_COLOR, bd=2, relief=RAISED, highlightthickness=0)
            self.realTimeDataTop.create_window(x+blockWidth-5, y, anchor=NE, window=window)
            self.motorStatus.append(window)
            
            
            #if k==4 or k==6 or k==7 or k==10: 
            id1 = self.realTimeDataTop.create_image(x+BALL_SHIFT_X, int(3*rowHeight/2), image=redBall, anchor=CENTER)
            if k==1:
                self.realTimeDataTop.bind('<Double-1>', self.onclick)
            id2 = self.realTimeDataTop.create_image(x+BALL_SHIFT_X, 3*rowHeight-int(rowHeight/2), image=redBall, anchor=CENTER)
            #else:
            #    id1 = self.realTimeDataTop.create_image(x+BALL_SHIFT_X, int(3*rowHeight/2), image=greenBall, anchor=CENTER)
            #    id2 = self.realTimeDataTop.create_image(x+BALL_SHIFT_X, 3*rowHeight-int(rowHeight/2), image=greenBall, anchor=CENTER)
            self.denserSignal.append(id1)
            self.wireTempSignal.append(id2)
            

            x += blockWidth
        
        #realTimeDataTop.create_text(firstSeparator+15+16, int(3*rowHeight/2)-8, fill="white", background="red", text="ON", anchor=NW)
        #w = realTimeDataTop
        #i=w.create_text(firstSeparator+15+16, int(3*rowHeight/2)-8, fill="cyan", text="ON", font=("Helvetica", 16), anchor=NW)
        #r=w. (w.bbox(i),fill="black")
        #w.tag_lower(r, i)
        
        gap = 12
        shift = 0
        realTimeWindowWidth = blockWidth-40
        realTimeWindowHeight = rowHeight-8
        
        x = firstSeparator
                 
        for k in range(13):
            
            self.realTimeDataTop.create_rectangle(x+blockWidth-realTimeWindowWidth-int(gap/2)-1, \
                2*rowHeight-realTimeWindowHeight-gap/2+2, x+blockWidth-int(gap/2)-1, \
                    2*rowHeight-gap/2+2, fill="black")
            

            self.denserText.append(self.realTimeDataTop.create_text(x+blockWidth-realTimeWindowWidth-int(gap/2)-1+int(realTimeWindowWidth/2),\
                                         2*rowHeight-realTimeWindowHeight-gap/2+2+int(realTimeWindowHeight/2)+shift, \
                                         fill=REAL_TIME_DATA_FILL, text="%.2f" % denserValue[k], font=REAL_TIME_DATA_FONT, anchor=CENTER))
            
            self.realTimeDataTop.create_rectangle(x+blockWidth-realTimeWindowWidth-int(gap/2)-1, \
                        3*rowHeight-realTimeWindowHeight-gap/2, x+blockWidth-int(gap/2)-1, \
                            3*rowHeight-gap/2, fill="black")
            
            
            self.wireTempText.append(self.realTimeDataTop.create_text(x+blockWidth-realTimeWindowWidth-int(gap/2)-1+int(realTimeWindowWidth/2),\
                                         3*rowHeight-realTimeWindowHeight-gap/2+int(realTimeWindowHeight/2)+shift, \
                                         fill=REAL_TIME_DATA_FILL, text="%.2f" % denserValue[k], font=REAL_TIME_DATA_FONT, anchor=CENTER))
                                         
            x += blockWidth
        
            
        for k in range(13):
                id = self.motorStatus[k].create_text(int(blockWidth/6)+2, int(rowHeight/3)+2, fill=MOTOR_OFF_FILL, text="OFF", anchor=CENTER)
                self.motorStatus[k].configure(bg=MOTOR_OFF_BG)
                self.motorStatusText.append(id)
        
        
        
        
    
        
        motorOnOf = Canvas(self.realTimeDataTop, width=firstSeparator-4, height=rowHeight-4)
        motorOnOf.configure(bg=REAL_TIME_PRO_TITLE_COLOR, bd=2, relief=RAISED, highlightthickness=0)
        self.realTimeDataTop.create_window(0, 0, anchor=NW, window=motorOnOf)
        
        motorOnOf.create_text(int((firstSeparator)/2),int((rowHeight)/2),fill="white",font=font, text="교반기 모터", anchor=CENTER)
        
        denserPressure = Canvas(self.realTimeDataTop, width=firstSeparator-4, height=rowHeight-4)
        denserPressure.configure(bg=REAL_TIME_PRO_TITLE_COLOR, bd=2, relief=RAISED, highlightthickness=0)
        self.realTimeDataTop.create_window(0, rowHeight, anchor=NW, window=denserPressure)
        
        denserPressure.create_text(int((firstSeparator)/2),int((rowHeight)/2),fill="white",font=font, text="덴서 압력", anchor=CENTER)
        
        wireTemp = Canvas(self.realTimeDataTop, width=firstSeparator-4, height=rowHeight-4)
        wireTemp.configure(bg=REAL_TIME_PRO_TITLE_COLOR, bd=2, relief=RAISED, highlightthickness=0)
        self.realTimeDataTop.create_window(0, rowHeight*2, anchor=NW, window=wireTemp)
        
        wireTemp.create_text(int((firstSeparator)/2),int((rowHeight)/2),fill="white",font=font, text="와이어 온도", anchor=CENTER)
        

        colorFrame = Frame(frame1, bg=BACKGROUNND, bd=0)  # used to get proper color btween the canvas top and below
        colorFrame.pack(expand=1, fill="x")
        self.realTimeDataBtm = Canvas(colorFrame, height=rowHeight*2, bg=REAL_TIME_DATA_BG, bd=0, highlightthickness=0)
        self.realTimeDataBtm.pack(expand=1, fill="x", pady=(8,0))
        
        
        
        diceAndDrumTemp = Canvas(self.realTimeDataBtm, width=firstSeparator-4, height=2*rowHeight-4)
        diceAndDrumTemp.configure(bg=REAL_TIME_PRO_TITLE_COLOR, bd=2, relief=RAISED, highlightthickness=0)
        self.realTimeDataBtm.create_window(0, 0, anchor=NW, window=diceAndDrumTemp)
        
        gap = 3
        diceAndDrumTemp.create_text(int((firstSeparator)/2),int((rowHeight)/2)+gap,fill="white",font=font, text="드럼", anchor=CENTER)
        diceAndDrumTemp.create_text(int((firstSeparator)/2),int((3*rowHeight)/2)-gap,fill="white",font=font, text="다이스", anchor=CENTER)
        
        
        x = firstSeparator
           
        # bottom bar contains drum and dice temperature values  
        for k in range(BLOCK_COUNT):
            self.realTimeDataBtm.create_line(x, 0, x, rowHeight*2, fill=BLOCK_SEPARATOR, width=2 )
            
            #if k==9 or k==10 or k==11: 
            id1 = self.realTimeDataBtm.create_image(x+BALL_SHIFT_X, rowHeight-int(rowHeight/2), image=redBall, anchor=CENTER)
            id2 = self.realTimeDataBtm.create_image(x+BALL_SHIFT_X, rowHeight+int(rowHeight/2), image=redBall, anchor=CENTER)
            #else:
            #    id1 = self.realTimeDataBtm.create_image(x+BALL_SHIFT_X, rowHeight-int(rowHeight/2), image=greenBall, anchor=CENTER)
            #    id2 = self.realTimeDataBtm.create_image(x+BALL_SHIFT_X, rowHeight+int(rowHeight/2), image=greenBall, anchor=CENTER)
            self.drumTempSignal.append(id1)
            self.diceTempSignal.append(id2)

            x += blockWidth


        gap = 12        
        shift = 0        
        x = firstSeparator    
        
        for k in range(13):
            self.realTimeDataBtm.create_rectangle(x+blockWidth-realTimeWindowWidth-int(gap/2)-1, \
                rowHeight-realTimeWindowHeight-gap/2+2, x+blockWidth-int(gap/2)-1, \
                    rowHeight-gap/2+2, fill="black")
            
            
            self.drumTempText.append(self.realTimeDataBtm.create_text(x+blockWidth-realTimeWindowWidth-int(gap/2)-1+int(realTimeWindowWidth/2),\
                                rowHeight-realTimeWindowHeight-gap/2+2+int(realTimeWindowHeight/2)+shift, \
                                         fill=REAL_TIME_DATA_FILL, text="%.2f" % denserValue[k], font=REAL_TIME_DATA_FONT, anchor=CENTER))
            
            self.realTimeDataBtm.create_rectangle(x+blockWidth-realTimeWindowWidth-int(gap/2)-1, \
                        2*rowHeight-realTimeWindowHeight-gap/2, x+blockWidth-int(gap/2)-1, \
                            2*rowHeight-gap/2, fill="black")
            
            
            self.diceTempText.append(self.realTimeDataBtm.create_text(x+blockWidth-realTimeWindowWidth-int(gap/2)-1+int(realTimeWindowWidth/2),\
                                    2*rowHeight-realTimeWindowHeight-gap/2+int(realTimeWindowHeight/2)+shift, \
                                         fill=REAL_TIME_DATA_FILL, text="%.2f" % denserValue[k], font=REAL_TIME_DATA_FONT, anchor=CENTER))
                                         
            x += blockWidth
            
        blockIdCanvas = Canvas(colorFrame, height=BLOCK_ID_CANVAS_HEIGHT, bg=BACKGROUNND, bd=0, relief=FLAT, highlightthickness=0)
        blockIdCanvas.pack(expand=1, fill="x")
        
        gap = 16
        x = firstSeparator
        for k in range(13):
            blockIdCanvas.create_rectangle(x+int(gap/2), 2, x+blockWidth-int(gap/2), BLOCK_ID_CANVAS_HEIGHT-8+2, fill="white", outline="")
            blockIdCanvas.create_text(x+int(blockWidth/2), 2+int((BLOCK_ID_CANVAS_HEIGHT-8)/2), text="#%d Block" % (k+1), fill="black", anchor=CENTER)
            x += blockWidth
        
    def onUpdate(self):
        
        blockData = self.dataManager.data.blockData
        
        
        
        #print("torque values are %s and %s" % (blockData[4].torque, blockData[6].torque))
        #self.realTimeDataTop.itemconfigure(self.denserText[3], text = "%.2f" % float(self.dataManager.val))
        
        firstSeparator = WINDOW_WIDTH-(MONITORING_NB_PAD_X*2) - 13*self.blockWidth - 2
        x = firstSeparator
        for k in range(13):
            y = 0
            index = []
            
            index.append(int(10.0*float(blockData[k].current/(MAX_CURRENT))))
            index.append(int(10.0*float(blockData[k].rpm/(MAX_RPM))))
            index.append(int(10.0*float(blockData[k].torque/(MAX_TORQUE))))
            index.append(0)
            index.append(0)
            
            
            
            for l in range(5):
                if index[l] > 9:
                    index[l] = 9
                
                y += int(self.blockHeight/6)
                self.DrawBar(self.barViewCanvas, x, y, index[l])
                
            x += self.blockWidth

        
        
        
               
        for k in range(BLOCK_COUNT):
            
            
            if blockData[k].rpm > 0.0:
                self.motorStatus[k].itemconfigure(self.motorStatusText[k], text="ON", fill=MOTOR_ON_FILL)
                self.motorStatus[k].configure(bg=MOTOR_ON_BG)
            else:
                self.motorStatus[k].itemconfigure(self.motorStatusText[k], text="OFF", fill=MOTOR_OFF_FILL)
                self.motorStatus[k].configure(bg=MOTOR_OFF_BG)
                
            val = 5.0       # to be modifed after the sensors will be added    
            if val < 0.0:    
                self.realTimeDataTop.itemconfigure(self.denserText[k], text = "Error", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            elif val < DENSER_PRESSURE_THRESHOLD:    
                self.realTimeDataTop.itemconfigure(self.denserText[k], text = "NA", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            else:
                pass
                

                
            if blockData[k].wire_temp < 0.0:    
                self.realTimeDataTop.itemconfigure(self.wireTempText[k], text = "Error", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            elif blockData[k].wire_temp < TEMPERATURE_THRESHOLD:    
                self.realTimeDataTop.itemconfigure(self.wireTempText[k], text = "NA", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            else:
                self.realTimeDataTop.itemconfigure(self.wireTempText[k], text = "%.2f" % blockData[k].wire_temp, fill=REAL_TIME_DATA_FILL, font=REAL_TIME_DATA_FONT)
                
                

            
            if blockData[k].drum_temp < 0.0:    
                self.realTimeDataBtm.itemconfigure(self.drumTempText[k], text = "Error", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            elif blockData[k].drum_temp < TEMPERATURE_THRESHOLD:    
                self.realTimeDataBtm.itemconfigure(self.drumTempText[k], text = "NA", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            else:
                self.realTimeDataBtm.itemconfigure(self.drumTempText[k], text = "%.2f" % blockData[k].drum_temp, fill=REAL_TIME_DATA_FILL, font=REAL_TIME_DATA_FONT)
                
            if blockData[k].dice_temp < 0.0:    
                self.realTimeDataBtm.itemconfigure(self.diceTempText[k], text = "Error", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            elif blockData[k].dice_temp < TEMPERATURE_THRESHOLD:    
                self.realTimeDataBtm.itemconfigure(self.diceTempText[k], text = "NA", fill="red", font=REAL_TIME_DATA_FONT_SMALL)
            else:
                self.realTimeDataBtm.itemconfigure(self.diceTempText[k], text = "%.2f" % blockData[k].dice_temp, fill=REAL_TIME_DATA_FILL, font=REAL_TIME_DATA_FONT)                


        for k in range(BLOCK_COUNT):
            self.UpdateSignal(self.realTimeDataBtm, self.drumTempSignal[k], blockData[k].drum_temp, DRUM_TEMP_LOW, DRUM_TEMP_HIGH)
            self.UpdateSignal(self.realTimeDataBtm, self.diceTempSignal[k], blockData[k].dice_temp, DICE_TEMP_LOW, DICE_TEMP_HIGH)        

    def UpdateSignal(self, canvas, signal, value, min, max):
        
        
        if value < TEMPERATURE_THRESHOLD:
            image = redBall
        elif value < min:
            image = greenBall
        elif value >= min and value < max:
            image = yellowBall
        else:
            image = redBall
            
        canvas.itemconfig(signal, image=image)
                    
    def Change(self):
        print("hello")
        #self.realTime.delete(self.ball1)
        #self.realTime.delete(self.ball2)
        #self.ball1 = self.realTime.create_image(150, 50, image=greenBall, anchor=CENTER)
        #self.ball12 = self.realTime.create_image(250, 50, image=greenBall, anchor=CENTER)
        
        

    def DrawBar(self, canvas, u, v, index):    
     
        gap = 3
        barWidth = int((MOTOR_INFO_BAR_WIDTH-8*gap)/9)
        color = [BAR_GREEN, BAR_YELLOW, BAR_RED]  

        for k in range (index):
             
            x = u+barWidth/2 + (barWidth+gap)*k + 6
            canvas.create_line(x, v-int(MOTOR_INFO_BAR_HEIGHT/2), x, v+int(MOTOR_INFO_BAR_HEIGHT/2), fill=color[int(k/3)], width=barWidth)
   
    
    
    
def run():
    #    root = Tk()
    
             
    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    SCREEN_X_CENTER = (SCREEN_WIDTH - WINDOW_WIDTH) / 2
    SCREEN_Y_CENTER = (SCREEN_HEIGHT - WINDOW_HEIGHT) / 2
    #root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT,
     #             SCREEN_X_CENTER, SCREEN_Y_CENTER))
     
    mycolor = '#%02x%02x%02x' % (64, 204, 208)
    
    root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
    
    root.configure(background=BACKGROUNND)

    root.resizable(False, False)
    
    root.title("Elicitor")
    
    
    dataManager = DataManager()
    try:
    
            
        dataManager.start()

 
        # Keep the main thread running, otherwise signals are ignored.
        
        View(root, dataManager)
    
    
    
        root.bind("<Key>", key)
    
        root.mainloop()
        
    except ServiceExit:
        print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

  
    dataManager.shutdown_flag.set()

     # Wait for the threads to close...
    dataManager.join()

 
        
    
 
 
    print('Exiting main program')


def key(event):
    print ("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        root.quit()


if __name__ == '__main__':
    run()


# tips:

"""
button1 = Button(self, text = "Quit", command = self.quit, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = canvas1.create_window(10, 10, anchor=NW, window=button1)
"""

