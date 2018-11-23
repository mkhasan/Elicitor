
import paho.mqtt.client as mqtt #import the client1
import threading
import time
import signal

from constants import *
from collections import namedtuple


import tkinter
from tkinter import messagebox

import os

from uuid import getnode as get_mac

class ProductionLine:
    setSpeed = 0
    curSpeed = 0
    BlockData = namedtuple("BlockData", ["rpm" , "current", "torque", "drum_temp", "dice_temp", "wire_temp"])
    blockData = []
    SpoolerData = namedtuple("SpoolerData", ["rpm", "current", "torque"])
    spoolerData = SpoolerData(rpm=0, current=0, torque=0)
    error = 0

    def __init__(self):
        for k in range(MAX_BLK):
            self.blockData.append(self.BlockData(rpm=0.0, current=0.0, torque=0.0, drum_temp=0.0, dice_temp=0.0, wire_temp=0.0))
            self.error = 0
    def Set(self, str):
        data = str.split(" ")
        if len(data) != (2+MAX_BLK*6+3):
            print("Data parsing Error (not enoght data element) !!!")
            return
            
        
        k = 0
        index = 0
        self.blockData = []
        
        try:

            self.setSpeed = int(data[k])

            self.curSpeed = int(data[k])

            k += 2
            index += 2
            

            for l in range(MAX_BLK):

               
                temp = self.BlockData(rpm=float(data[k+6*l+0]), current=float(data[k+6*l+1])/10.0, torque=float(data[k+6*l+2])/10.0, \
                                       drum_temp=float(data[k+6*l+3]), dice_temp=float(data[k+6*l+4]), wire_temp=float(data[k+6*l+5]))
                self.blockData.append(temp)
                
                
                index += 6
                #print("index is %d" %l)
                #print(self.blockData)
        
                        
            self.spoolerData= self.SpoolerData(float(data[index]), float(data[index+1])/10.0, float(data[index+2])/10.0)
            #self.spoolerData.current = 2 #int(data[index+1])
            #self.spoolerData.torque = 3 #int(data[index+2])        
            
        except Exception:
            print("Data parsing Error (format not matched) !!!")
            return

        #print(len(self.blockData))
    def PrintData(self):
        
        print("set speed %d current speed %d" % (self.setSpeed, self.curSpeed))
        for k in range (MAX_BLK):
            print (self.blockData[k])
        print(self.spoolerData)
            
class DataManager(threading.Thread):
    
    
    data = ProductionLine() 

    def __init__(self):
        super(DataManager, self).__init__()
        self.shutdown_flag = threading.Event()
        
    def run(self):
        try:
            
            broker_address=SERVER_ADDR
            #broker_address="iot.eclipse.org"
            print("creating new instance")
            client = mqtt.Client("%s%d%s" %(type(self).__name__,os.getpid(),get_mac()))#create new instance
            client.on_message=self.on_message #attach function to callback
            print("connecting to broker")
            client.connect(broker_address) #connect to broker
            
            print("Subscribing to topic %s " % TOPIC_ALL_DATA)
            client.subscribe(TOPIC_ALL_DATA)
            
                    
            client.loop_start()
            while not self.shutdown_flag.is_set():
                
                time.sleep(2)
                
                
            
            print("Exiting client")  
            client.loop_stop()
            client.disconnect()
        except Exception:
            print("Connection Error !!!")
            self.data.error = 1
            #messagebox.showinfo("Information","Informative message")
    
    ############
    def on_message(self, client, userdata, message):
        
        
        payload = str(message.payload.decode("utf-8"))
        #print("message received %s" % payload)
        #print("message topic=",message.topic)
        #print("message qos=",message.qos)
        #print("message retain flag=",message.retain)
        #print("%.20f    %.20f" % (on_message.now, on_message.prev))
        
        
        self.data.Set(payload)
        
        """
        try:
            y = payload.split(" ")
            self.val = int(y[0])
        except Exception:
            self.val = -1
        """
        
        #print("val is %d " % self.val)
    ########################################    
        
class ServiceExit(Exception):
    pass

def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServiceExit

def main():
 
   
    #path = "%s../Echo" % os.path.dirname(os.path.abspath(__file__))
    # Register the signal handlers
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
    
    
    #d = ProductionLine()
    
    #str = "100 100 0 0 0 15.7066 15.65 0 0 0 0 20.2442 17.8122 0 0 0 0 17.1122 17.582 0 0 0 0 19.3856 14.7896 0 1418 391 371 19.6498 21.4686 0 1446 344 333 17.414 19.2158 0 1488 404 375 67.3258 24.3476 0 1508 344 326 20.6308 17.3196 0 1553 393 365 20.1214 17.114 0 1549 343 315 21.2252 21.8346 0 1593 394 345 19.5838 16.6122 0 1606 337 237 23.291 21.7062 0 0 0 0 0 0 0 0 0 0 0 0 0 663 394 192"
    
    #d.Set(str)
    #d.PrintData()
    #return
    
 
    print('Starting main program')
 
    # Start the job threads
    try:
        j1 = DataManager()
        j1.start()

 
        # Keep the main thread running, otherwise signals are ignored.
        while True:
            time.sleep(0.5)
 
    except ServiceExit:
        # Terminate the running threads.
        # Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
        j1.shutdown_flag.set()

   # Wait for the threads to close...
        j1.join()
 
 
    print('Exiting main program')
 
 
if __name__ == '__main__':
    main()
        