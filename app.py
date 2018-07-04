from iexfinance import get_historical_data, Stock
import pandas as pd
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()
ticker = pd.read_csv('tickers.csv', index_col="Symbol")

#HTML Layout
app.layout = html.Div(children=[
            
                html.H1(className='text-center', children="""
                    STOCK TRACKER
                    """),
                #Using bootstrap theme 
		        html.Div(className='container', 
		                children=[html.Hr(), html.Div(className ='row', 

                        #Ticker column
                        children=[html.Div(className ='col-lg-4',
                        children=[html.Form(
                        children=[html.Fieldset(
                        children=[html.Div(className ='form-group', 
                        children=[html.Label(children="""TICKER"""),
                        dcc.Input(id='input', className='form-control',value='', type='text')]
                        )]
                        )])]),

                        #Graph column
                        html.Div(className='col-lg-8',
                        children=[html.Div(id='output_graph')])])])


])

app.css.append_css({"external_url": '/static/bootswatch.css'})
app.css.append_css({"external_url": '/static/styles.css'}) #stylesheet used

#Functions
def change_pct(open_price,current_price):
    pct = ((current_price-open_price)/open_price)*100
    pct_string = str(round(pct,2))+"%"
    return pct_string

@app.callback(
Output(component_id='output_graph', component_property='children'),
[Input(component_id='input', component_property='value')])
def update_graph(input_data):
    start_date = dt.datetime(2017,1,1)
    end_date = dt.datetime.now()
    input_data = str(input_data).upper()

    #Get request for API
    name = ticker.loc[input_data, "Company"] 
    df = get_historical_data(str(input_data).upper(),start_date=start_date, end_date=end_date, output_format='pandas')
    tick = Stock(input_data)
    
    # Graph layout
    return [dcc.Graph(
            id='stocks_graph',
            figure={
            'data':[{'x':df.index, 'y':df.close, 'type':'line', 'name':input_data}],
            'layout':{'title':str(name)}}),
            html.Div(className='container',children=[
            html.Div(className="row", children=[
            html.Div(className="col-sm-2", children=[
            html.H1(className="center-align",children=[tick.get_price()])]),
            html.Div(className="col-sm-2", children=[
            html.H5(className="center-align",children=[change_pct(df.close[-2],tick.get_price())])]),
            html.Div(className="col-sm-2", children=[
            html.H6(className="center-align",children=["Open"]), html.H4(className="center-align",children=[tick.get_open()])]),
             html.Div(className="col-sm-2", children=[
            html.H6(className="center-align",children=["High"]), html.H4(className="center-align",children=[df.high[-1]])]),
              html.Div(className="col-sm-2", children=[
            html.H6(className="center-align",children=["Low"]), html.H4(className="center-align",children=[df.low[-1]])]),
               html.Div(className="col-sm-2", children=[
            html.H6(className="center-align",children=["Volume"]), html.H4(className="center-align",children=[df.volume[-1]])])
            ])])
           ]

if __name__ == '__main__':
    app.run_server(debug=True)
