import numpy as np
import pyautogui as gui
import time


class Working:
    """
    arguments:
     - time: float, Total minutes you are working
     - sleep: interval between mouse movement 
     
    Methods:
        work(): execute the movement of mouse during the time with a 
        interval of sleep. 
        
     """
    def __init__(self,time,  sleep=10):
        self.sleep = sleep
        #minutos 60*60
        self.time = time
        self.total = int((self.time*60) /self.sleep)
    
    def move(self):
        x =  np.random.randint(500, 1080)
        y =  np.random.randint(400,800)
        gui.click(x, y, clicks=0)
        time.sleep(self.sleep)
    
    def work(self):
        print(f"Vamos a trabajar: {self.time} minutos.")
        totalus = self.time*60
        for i in range(self.total):
            self.move()
            totalus -= self.sleep
            print(f"Quedan {totalus/60} minutos")
            
            
matute = Working(time = 60)
matute.work()