import yfinance as yf
import dash
from dash import html,dcc 
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([ 
    html.H1(children = 'Stock Market Plots -  Utkarsh Gaikwad',
            style = {'textAlign':'center'}
    ),

    html.Br(),
    html.Br(),

    html.Label('Enter Stock Ticker : '),
    dcc.Input(
        id = 'ticker',
        placeholder='Ticker Name',
        value= '',
        type = 'text'
    ),

    html.Br(),
    html.Br(),

    dcc.Dropdown(
        id = 'period',
        options = [
            {'label':'1 Year','value':'1y'},
            {'label':'5 Years','value':'5y'},
            {'label':'Maximum','value':'max'}
        ]
    ),

    html.Br(),
    html.Br(),

    html.Button(children='Show Plot',id='Button',n_clicks=0),
    dcc.Graph(id='graph-output',figure={})
])

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    [Input(component_id='Button',component_property='n_clicks')],
    [State(component_id='ticker',component_property='value'),
     State(component_id='period',component_property='value')],
    prevent_initial_call=True
)
def candlestickplot(n,val_chosen,prd):
    if len(val_chosen)>0:
        print(n)
        print('Value User Chose : ',val_chosen)
        print('Period Chosen : ',prd)
        df = yf.download(val_chosen, period=prd,interval='1d')
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                        open=df['Open'],
                                        high=df['High'],
                                        low=df['Low'],
                                        close=df['Close']),
                        ])
        title = {
         'text': val_chosen+" Candlestick Chart",
         'y':0.9,
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top' 
        }

        fig.update_layout(xaxis_rangeslider_visible=False,
                 title=title,
                 yaxis_title=val_chosen+" Stock Price")

        return fig


if __name__ == '__main__':
    app.run_server(debug=True)