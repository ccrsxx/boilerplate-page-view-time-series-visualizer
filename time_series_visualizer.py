import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
     & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df, color='#c52728')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).value.mean().unstack()
    df_bar.columns = pd.to_datetime(df_bar.columns, format='%m').month_name().to_list()
    df_bar.index.name, df_bar.columns.name = 'Years', 'Months'

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))

    df_bar.plot.bar(ax=ax)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%m') for d in df_box.date]

    # # Draw box plots (using Seaborn)
    fig, ((ax0, ax1)) = plt.subplots(figsize=(18, 8), nrows=1, ncols=2)

    sns.boxplot(x=df_box.date.dt.year, y=df_box.value, ax=ax0)

    ax0.set_title('Year-wise Box Plot (Trend)')
    ax0.set_xlabel('Year')
    ax0.set_ylabel('Page Views')

    df_box.sort_values(by='month', inplace=True)
    df_box['month'] = pd.to_datetime(df_box.month, format='%m').dt.strftime('%b')

    sns.boxplot(x=df_box.month, y=df_box.value, ax=ax1)

    ax1.set_title('Month-wise Box Plot (Seasonality)')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Page Views')

    # # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
