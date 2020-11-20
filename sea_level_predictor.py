import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import math

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x,y=df["Year"],df["CSIRO Adjusted Sea Level"]
    
    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1=linregress(x=x,y=y)
    regression_line_1=[(slope1*x)+intercept1 for x in range(1880,2050)]

    # Create second line of best fit
    x_r,y_r=df[df["Year"]>=2000]["Year"],df[df["Year"]>=2000]["CSIRO Adjusted Sea Level"]
    slope2, intercept2, r_value2, p_value2, std_err2=linregress(x=x_r,y=y_r)

    regression_line_2=[(slope2*x)+intercept2 for x in range(2000,2050)]


    full_years=list(range(1880,2050))
    modern_years=list(range(2000,2050))

    plt.scatter(x,y)
    plt.plot(full_years,regression_line_1,c="red")
    plt.plot(modern_years,regression_line_2,c="green")  


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
