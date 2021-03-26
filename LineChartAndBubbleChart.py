import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Line Chart
line_df = df2
line_df['date'] = pd.to_datetime(line_df['date'])
data_linechart = [go.Scatter(x=df2['date'], y=df2['actual_max_temp'], mode='lines', name='Max Temperature')]

# Bubble chart
bubble_df = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#bubble_df['Unrecovered'] = bubble_df['Confirmed'] - bubble_df['Deaths'] - bubble_df['Recovered']
#bubble_df = bubble_df[(bubble_df['Country'] != 'China')]
#bubble_df = bubble_df.groupby(['Country']).agg(
  #  {'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()
data_bubblechart = [
    go.Scatter(x=df2['average_min_temp'],
               y=df2['average_max_temp'],
               text=df2['date'],
               mode='markers', marker=dict(size=8, color='red'))]



