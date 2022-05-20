#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64




# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    html.Div([
        dcc.Input(
            id= 'name',
            placeholder='Enter a value...',
            type='text',
            value=''
        )],
        style={'width': '48%', 'display': 'inline-block', 'backgroundColor': 'black'}),
    html.Hr(),
    html.Div([
        dcc.RangeSlider(-5, 5, 1, count=1, value=[-2, 2], id='slider_val')
        ]),
    html.Hr(),
    html.Div(id='Output',style={
        'color': 'white'})
],style={'backgroundColor': 'black'})





#app.layout = html.Div([
#    dcc.Markdown(children=markdown_text)
#])







# Create a Dash callback:
@app.callback(
    Output('Output', 'children'),
    [Input('name', 'value'),
     Input('slider_val', 'value')])
def callback_a(name,sl_values):
    return '**{}** is selected two values that their sum is "{}"'.format(name,sl_values[0]+sl_values[1])





# Add the server clause:
if __name__ == '__main__':
    app.run_server()
