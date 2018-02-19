###This was designed to be a basic form of a live dynamic tracking system for multiple figures at once.
###Libraries
import dash
from dash.dependencies import Output,Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
###Deques
X = deque(maxlen=50)
X.append(1)
Y = deque(maxlen=50)
Y.append(2)
X2 = deque(maxlen=50)
X2.append(1)
Y2 = deque(maxlen=50)
Y2.append(1.75)
X3 = deque(maxlen=50)
X3.append(1)
Y3 = deque(maxlen=50)
Y3.append(0.68)
RX = deque(maxlen=50)
RX.append(1)
RY = deque(maxlen=50)
RY.append(1)
###Dash Base
app=dash.Dash(__name__)
app.title='Business Course Generator'
app.layout=html.Div([
    dcc.Graph(id='live-graph',animate=True),
    dcc.Interval(
        id='graph-update',
        interval=1*820
    )
])
###Callback
@app.callback(Output('live-graph','figure'),
              events = [Event('graph-update','interval')])
###Main Definition
def update_graph_scatter():
    ###Globals for Deques
    global X , X2, X3, RX
    global Y , Y2, Y3, RY
    ###Generators
    X.append(X[-1]+1)
    X2.append(X2[-1]+1)
    X3.append(X3[-1]+1)
    RX.append(RX[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.15,0.15))
    Y2.append(Y2[-1]+Y2[-1]*random.uniform(-0.15,0.15))
    Y3.append(Y3[-1]+Y3[-1]*random.uniform(-0.15,0.15))
    RY.append(RY[-1]+RY[-1]*random.uniform(-.01,.01))
    ###Scatter plotly details
    data1 = plotly.graph_objs.Scatter(
        x = list(X),
        y = list(Y),
        name='Varient 1',
        mode='lines',
        ###Style
        fill='tozeroy',
        fillcolor='rgba(200,80,200,.3)',
        line=dict(
            color=('rgb(42,42,210)'),
            dash='line',
            shape='spline')
    )
    data2 = go.Scatter(
        x = list(X2),
        y = list(Y2),
        name="Varient 2",
        mode='lines',
        fill='tozeroy',
        ###Style
        fillcolor='rgba(200,200,80,0.3)',
        line=dict(
            color=('rgb(42,210,42)'),
            dash='line',
            shape='spline'
        )
    )
    data3 = go.Scatter(
        x = list(X3),
        y = list(Y3),
        name="Varient 3",
        mode='lines',
        ###Style
        fill='tozeroy',
        fillcolor='rgba(80,200,200,0.3)',
        line=dict(
            color=('rgb(210,42,42)'),
            dash='line',
            shape='spline'
        )
    )
    data4 = go.Scatter(
        x = list(RX),
        y = list(RY),
        name="Base",
        mode='lines',
        ###Style
        fill='tozeroy',
        fillcolor='rgba(255,255,255,0.3)',
        line=dict(
            color=('rgb(42,42,42)'),
            dash='line',
            shape='none'
        )
    )
    ###Main graph layout and options
    return {'data':[data4,data1,data2,data3], 'layout':go.Layout(xaxis=dict(range=[min(min(X), min(X2),min(X3),min(RX)),max(max(X), max(X2), max(X3),max(RX))]), 
                                              yaxis=dict(range=[min(min(Y), min(Y2), min(Y3),min(RY)),max(max(Y), max(Y2), max(Y3),max(RY))]),
                                              plot_bgcolor='rgb(210,210,210)',
                                              showlegend=True
                                              )}
#Run Server
if __name__=='__main__':
    app.run_server(debug=True)