# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is the data for the Annual change in house prices displayed per month
#The data shows the price changes from the year 2006 to 2022



def line(df):
    """
    Takes the dataframe parameter and creates a line plot
    """
    plt.figure(figsize=(20,10))
    plt.plot(housep["Date"],housep["Percent Change"])
    plt.xlabel("Date")
    plt.ylabel("Percent Change")
    plt.legend()
    plt.xlim("2006 Feb", "2022 Aug") #removing whitespace
    plt.xticks(housep["Date"][::12]) #reducing x axis labes
    #setting custom ylim
    plt.ylim(min(housep["Percent Change"]),
             max(housep["Percent Change"]))
    #setting custom ytick range
    plt.yticks(np.arange(min(housep["Percent Change"]),
                         max(housep["Percent Change"]))) 
    plt.savefig("Figure1.png")
    plt.show()

def histogram(df):
    """
    Takes the dataframe parameter and creates a histogram
    """
    plt.figure()
    plt.hist(housep["Percent Change"])
    plt.title("Percent Change Histogram")
    plt.xlabel("Percent Change")
    plt.ylabel("Frequency")
    plt.savefig("Figure2.png")
    plt.show()

def violin(df):
    """
    Takes the dataframe parameter and creates a violinplot
    """
    plt.figure()
    plt.violinplot(housep["Percent Change"])
    plt.title("Percent Change Violin Plot")
    plt.xlabel("Density")
    plt.ylabel("Percent Change")
    plt.savefig("Figure3.png")
    plt.show()

if __name__ == "__main__":
    
    housep = pd.read_csv("firste.csv",header=7,
                         names=["Date","Percent Change"])
    line(housep)
    
    histogram(housep)
    
    violin(housep)
    
    