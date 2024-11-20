import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

global data
data = None

def load_and_clean_data():
    global data
    data = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    data = data[(data['value'] > data['value'].quantile(0.025)) & (data['value'] < data['value'].quantile(0.975))]
    return data

load_and_clean_data()

# Function to draw a line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.grid(True)
    plt.show()
    return fig

# Function to draw a bar plot
def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    df = data.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    df_grouped.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[pd.to_datetime(str(x), format='%m').strftime('%B') for x in range(1, 13)])
    plt.show()
    return fig

# Function to draw box plots
def draw_box_plot():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    df = data.copy()
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    df['month_num'] = df.index.month
    df = df.sort_values('month_num')

    sns.boxplot(x='year', y='value', data=df, ax=axs[0])
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df, ax=axs[1])
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    plt.show()
    return fig
