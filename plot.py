
import matplotlib.pyplot as plt 

import datetime
import os
import sys

from collections import namedtuple
from numpy import block
import statistics 

BlockData = namedtuple("BlockData", ["elapsed_sec", "set_speed", "cur_speed", "rpm" , "current", "torque", "drum_temp", "dice_temp", "wire_temp"])

def GetData():

    index_rpm = 3
    
    home = "HOME"
    try:  
       path = os.environ[home]
    except KeyError: 
       print ("Please set the environment variable "+home)
       sys.exit(1)
    
    if index_rpm == 1:
        path += "/temp/data1"
    else: 
        path += "/temp/data"
    
    if len(sys.argv) > 1: 
        pass #print(sys.argv)
    else:
       print ("arg does not contain block no")
       sys.exit(1)
    
    path += "/block_" + sys.argv[1] + ".txt"
    
    #print(path)
    data_file = open(path,'r')
            
    
    turn = 0
    skip = 100


    blockData = BlockData(elapsed_sec=[], set_speed=[], cur_speed=[], rpm=[], current=[], torque=[], drum_temp=[], dice_temp=[], wire_temp=[])
        
    firstData = True
    
    #ts = '2013-01-12 15:27:43'
    format = '%Y-%m-%d %H:%M:%S'
    start = datetime.datetime.now()
    while  True:

        
        line = data_file.readline()
        
        #print(len(line)) 
        
        if len(line) == 0:
            break
        
        if len(line) > 1 and turn == 0:
            
            data = line.split("\t")
            #data[7] = "2018-08-21 12:17:42"
            if int(data[index_rpm]) > 0 or firstData == False:
                date_time = data[index_rpm+6].split()
                #print(date_time[1])
                now = datetime.datetime.strptime(date_time[0] + " " + date_time[1], format)
                
                if firstData == True:
                    start = now
                    firstData = False 
    
                blockData.elapsed_sec.append((now-start).total_seconds()) 
                
                blockData.set_speed.append(float(data[1]))
                blockData.cur_speed.append(float(data[2])*1.0)
                blockData.rpm.append(float(data[index_rpm]))
                blockData.current.append(float(data[index_rpm+1])/10.0)
                blockData.torque.append(float(data[index_rpm+2])/10.0)
                blockData.drum_temp.append(float(data[index_rpm+3]))
                blockData.dice_temp.append(float(data[index_rpm+4]))
                blockData.wire_temp.append(float(data[index_rpm+5]))
                
                
                
                #print(data[5])
                #print("%s %s" % (data[6], data[7]) )
                
        
        turn = (turn+1)%skip
        
            
            
    
    
    return blockData

def PrintList(list):
    for count in range(len(list)):
        print(list[count])
        
def PrintStatistics(data):
    THRESHOLD = 5.0
    
    trData = BlockData(elapsed_sec=[], set_speed=[], cur_speed=[], rpm=[], current=[], torque=[], drum_temp=[], dice_temp=[], wire_temp=[])

    
    if len(sys.argv) > 2:
        print("\nblock %s  statistics" % sys.argv[1])
        
        for k in range(len(sys.argv)):
            if k < 2:
                continue
        
        
            if sys.argv[k] in BlockData._fields:
                index = BlockData._fields.index(sys.argv[k])
                #print(len(data[index]))
                for count in range(len(data[index])):
                    if data.cur_speed[count] >= THRESHOLD:
                        trData[index].append(data[index][count])  
            
            avg = statistics.mean(trData[index])
            stdev = statistics.stdev(trData[index])
            #PrintList(trData[index])
                
            print("\n%s statistics \n" % BlockData._fields[index])
            print("%8s%8s" %("mean", "stdev"))
            print("%8.2f%8.2f" % (avg, stdev))
            

                    

def main():

# importing the required module

    blockData = GetData()  
    #return    
    # plotting the points
    
    PrintStatistics(blockData)
    
    for count in range(len(BlockData._fields)):
        if BlockData._fields[count] in sys.argv:
            plt.plot(blockData.elapsed_sec, blockData[count], label=BlockData._fields[count])
    
         
    #print("len is %d" % len(trData.rpm))
    
    

            #avg = statistics.mean(trData[index])
            #stdev = statistics.stdev(trData[index])
            #PrintList(trData[index])
                
            #print("%s statistics" % BlockData._fields[index])
            #print("%10s%10s" %("mean", "stdev"))
            #print("avg %8.2f stdev %8.2f" % (avg, stdev))

                    
    
        
        
    #index = BlockData._fields.index(sys.argv[2])
    
    #print("index of %s is %d" % (sys.argv[2], index))
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
      
    # giving a title to my graph 
    plt.title('KWSA Data ' + "block " + sys.argv[1]) 
   
    plt.legend() 
   
    plt.show()
    #print("done")
    plt.close()
    #print('HELLO')

def key(event):
    print ("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        plt.close()

if __name__ == '__main__':
    main()