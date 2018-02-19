###This was mainly made to test the pandas_datareader library.
###Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader as web
import datetime
###Base info
start = datetime.datetime(2000,1,1)
end = datetime.datetime.now()
stock='GOOG'
df= web.DataReader(stock,'google',start,end)
###Dash Base
app = dash.Dash()
app.title='Dynamic Stock Tracker'
app.layout = html.Div(children=[
    html.Div(children='''
        Stock
        '''),
    dcc.Input(id='input',value='',type='text'),
    html.Div(id='output-graph')
    ])
###Callback
@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input',component_property='value')]
    )
###Main Definition
def update_graph(input_data):
    ###Update Data
    start = datetime.datetime(2000,1,1)
    end = datetime.datetime.now()
    df= web.DataReader(input_data,'google',start,end)
    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x':df.index,'y':df.High,'type':'line','name':input_data}
            ],
            'layout':{
                'title':input_data
            }
        }
    )
###Run Server
if __name__ == '__main__':
    app.run_server(debug=True) 