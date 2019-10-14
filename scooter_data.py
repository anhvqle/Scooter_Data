# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def readScooterData(numRows = None):
    df = pd.read_csv("xtern_data.csv", nrows=numRows)
    return df

def main():
    scooterDF = readScooterData()
    
    #Adding an Operation_Time columnn for the dataset
    
    opTime = scooterDF.loc[:,"power_level"].map(lambda x: 5-x)
    scooterDF["Operation_Time"] = opTime
    return scooterDF
    
    x = scooterDF.loc[:, 'xcoordinate']
    y = scooterDF.loc[:, 'ycoordinate']
    
    plt.title('Scooter Location')
    plt.xlabel('x coordinate') # add x label
    plt.ylabel('y coordinate') # add y label
    plt.scatter(x,y)
    plt.show()