import numpy as np
import math
import serial
from GUI import variable
def BT(port_num,speed):
    global variable
    
    ser = serial.Serial(
            # Serial Port to read the data from
            port=port_num,
     
            #Rate at which the information is shared to the communication channel
            baudrate = speed,
       
            #Applying Parity Checking (none in this case)
            parity=serial.PARITY_NONE,
     
           # Pattern of Bits to be read
            stopbits=serial.STOPBITS_ONE,
         
            # Total number of bits to be read
            bytesize=serial.EIGHTBITS,
     
            # Number of serial commands to accept before timing out
            timeout=1
    )
    a= []
    # Pause the program for 1 second to avoid overworking the serial port
    while(1):
            x=ser.read(1)
            #print(x)
            a.append(x.decode("utf-8"))
            if(a == "1"):
                variable["I"].set("Dolphin")
                variable["W"].set("".join(a))
            else:
                variable["I"].set("Dalton")
                variable["W"].set("".join(a))
                


    ser.close()
