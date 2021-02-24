#!/bin/python3
import os
import time 
print(1)
#os.system('echo "hi" ; sleep 2  ; echo "tc"  ')
#os.system(' echo "das" ' )
os.system('./tgrMqttClass.py --pub "toggle1" &')
time.sleep(5)
print(2)

