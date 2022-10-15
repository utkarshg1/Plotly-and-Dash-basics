import dash
from dash import html, dcc

app = dash.Dash()

colors = {
    'text':'#0000FF',
    'plot_bgcolor':'#00FFFF',
    'paper_bgcolor':'#00FFFF'
}

app.layout = html.Div([
    html.H1(children='Hello Utkarsh!',
            style = {
                'textAlign':'center',
                'color': colors['text']                
            }
    ),

    html.Div(children='Welcome to Dash by Plotly.',
            style = {
                'textAlign':'center',
                'color': colors['text']
            }
    ),

    dcc.Graph(
        id = 'SampleChart',
        figure = {
            'data': [
                {'x':[4,6,8],'y':[12,16,18],'type':'bar','name':'First Chart'},
                {'x':[4,6,8],'y':[20,24,26],'type':'bar','name':'Second Chart'}
            ],
            'layout' : {
                'plot_bgcolor':colors['plot_bgcolor'],
                'paper_bgcolor':colors['paper_bgcolor'],
                'font':{
                    'color':colors['text']
                },
                'title':'Simple Bar Chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)