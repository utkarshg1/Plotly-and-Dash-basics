import dash
from dash import dcc, html 
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(21)
x_rand = np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

app.layout = html.Div([
    dcc.Graph(
        id = 'Scatterplot',
        figure = {
            'data':[
                go.Scatter(
                    x = x_rand,
                    y = y_rand,
                    mode = 'markers'
                )
            ],
            'layout': go.Layout(
                title = 'Scatterplot of Random 60 points',
                xaxis = {'title':'Random X values'},
                yaxis = {'title':'Random Y values'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug='True')