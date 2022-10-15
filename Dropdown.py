import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Choose a City : '),
    dcc.Dropdown(
        id = 'FirstDropdown',
        options =[
            {'label':'San Fransisco', 'value':'SF'},
            {'label':'New York City', 'value':'NYC'},
            {'label':'Raleigh Durham', 'value':'RDU'}
        ],
        placeholder='Select Your City',
        multi=True
    ),

    html.Br(),
    html.Br(),

    html.Label('This is a Slider'),
    dcc.Slider(
        min = 1,
        max = 10,
        value=5,
        step= 0.5           
    ),

    html.Br(),
    html.Br(),

    html.Label('This is a Range Slider'),
    dcc.RangeSlider(
        min = 1,
        max = 10,
        step = 0.5,
        value = [3,7]
    ),

    html.Br(),
    html.Br(),

    html.Label('This is a Input Box : '),
    dcc.Input(
        placeholder='Enter your Name',
        type = 'text',
        value=''
    ),

    html.Br(),
    html.Br(),

    html.Label('This is a Text Area'),
    html.Br(),
    html.Br(),
    dcc.Textarea(
        placeholder='Give a feedback',
        style = {'width':'100%'}
    ),

    html.Br(),
    html.Br(),

    html.Button('Submit',id='Button1')
])

if __name__=='__main__':
    app.run_server(debug=True)