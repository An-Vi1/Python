#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import normal
import pandas as pd

#%%

class MakeDataFiles:
    
    def __init__(self):
        
        # Experiment - 1
        # self.x,  self.y  = [-1, 1], [0, 0]
        # self.Vx, self.Vy = [0, 0], [-0.5, 0.5]
        # self.M = [1, 1]
        
        # Experiment - 2
        # self.x,  self.y  = [-1, 0], [1, 0]
        # self.Vx, self.Vy = [1.2, 0], [0, 0]
        # self.M = [1, 4]
        
        # Experiment - 3
        self.x,  self.y  = [-1, 0, 1], [0, 0, 0]
        self.Vx, self.Vy = [0, 0, 0], [1, -1, 0]
        self.M = [1, 1, 1]
    

    def WriteDataFiles(self):
        
        M_data  = open(r'Data/M.txt', 'w')
        x_data  = open(r'Data/x.txt', 'w')
        y_data  = open(r'Data/y.txt', 'w')
        vx_data = open(r'Data/vx.txt','w')
        vy_data = open(r'Data/vy.txt','w')
        
        np.savetxt(M_data,  np.array([self.M])  )
        np.savetxt(x_data,  np.array([self.x])  )
        np.savetxt(y_data,  np.array([self.y])  )
        np.savetxt(vx_data, np.array([self.Vx]) )
        np.savetxt(vy_data, np.array([self.Vy]) )
        
        M_data.close()
        x_data.close()
        y_data.close()
        vx_data.close()
        vy_data.close()
        

#%%

if __name__ == '__main__':
    
    DoMyWork = MakeDataFiles()
    DoMyWork.WriteDataFiles()
