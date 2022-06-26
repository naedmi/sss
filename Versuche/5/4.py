import math
import time
import redlab as rl 

value = 0 
while True:
    sinus = math.sin(value) + 1 
    value += 0.1 
    rl.cbVOut(0, 0, 101, sinus) 
    time.sleep(1/100)