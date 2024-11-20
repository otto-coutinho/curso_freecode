import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Prepare extended year range for predictions
    years_extended = pd.Series(range(1880, 2051))  # Extended years to 2050

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, res.intercept + res.slope*years_extended, 'r')

    # Create second line of best fit for years from 2000 to the most recent year
    new_df = df[df['Year'] >= 2000]
    res_new = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended[years_extended >= 2000], res_new.intercept + res_new.slope*years_extended[years_extended >= 2000], 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
