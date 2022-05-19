#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go




colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# Launch the application:
app=dash.Dash()

# Create a DataFrame from the .csv file:
df=pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\Dashes\OldFaithful.csv")

# Create a Dash layout that contains a Graph component:
app.layout=html.Div([dcc.Graph(id='first_exercise',
                               figure = {'data':[
                                       go.Scatter(
                                       x=df['X'],
                                       y=df['Y'],
                                       text=df['D'],
                                       mode='markers',
                                       marker = {
                                           'size':df['D'],
                                           'color': df['D'],
                                           'line':{'width':2,
                                           'color':'black'},
                                           'showscale':True,
                                           'colorscale':'Jet'
                                       }
                                       )],
                               'layout':go.Layout(title='My_first_dash',
                                                   xaxis = {'title':'duration of the current eruption in minutes'},
                                                   yaxis = {'title':' waiting time until the next eruption in minutes'},
                                                       )}
                               )])

if __name__ == '__main__':
    app.run_server()




















# Add the server clause:
