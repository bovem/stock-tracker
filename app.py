from iexfinance import get_historical_data
import pandas as pd
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time


app = dash.Dash()

#FOR FETCHING COMPANY NAME FROM TICKER SYMBOL
ticker = pd.read_csv('spreadsheet/tickers.csv', index_col="Symbol")

#HTML Layout
app.layout = html.Div(children=[
             #ADDRESS BAR
             dcc.Location(id='url', refresh=False),

             #NAVIGATION BAR
             html.Div(className="container top-navbar", 
                     children=[html.Nav(className=["navbar navbar-expand-lg navbar-light bg-light"],
                     children=[html.A(className='navbar-brand', href="/",
                     children=["""Stock Tracker"""])])]),html.Div(id='page-content') 
            ])

#STYLESHEETS    
app.css.append_css({"external_url": '/static/stylesheets/bootswatch.css'})
app.css.append_css({"external_url": '/static/stylesheets/styles.css'})

#FOR EXCEPTIONS CALLED BY TWO CALLBACK FUNCTIONS
app.config['suppress_callback_exceptions']=True 
                                                
#FUNCTIONS
def pct_change(open_price,current_price):
    pct = ((current_price-open_price)/open_price)*100
    return pct

def pct_change_formatter(pct_change):
    PCT_COLOR = "center-align text-danger"
    if pct_change>0:
        pct_string = "+"+str(round(pct_change,2))+"%"
        PCT_COLOR = "center-align text-success"
    else:    
        pct_string = str(round(pct_change,2))+"%"
    return (pct_string, PCT_COLOR)

#TO SWITCH PAGES
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == "/":

        #STOCKS APP
        return html.Div([
            html.Div(className='container', 
                            children=[html.Hr(className="seperator"), html.Div(className ='row', 

                            #TICKER COLUMN
                            children=[html.Div(className ='col-lg-12',
                            children=[html.Form(
                            children=[html.Fieldset(
                            children=[html.Div(className ='form-group', 
                            children=[html.Label(children="""Ticker"""),
                            dcc.Input(id='input', className='form-control',value='', type='text')]
                            )]
                            )])])]),

                            #GRAPH COLUMN
                            html.Div(className="row", children=html.Div(className='col-lg-12',
                            children=[html.Div(id='output_graph')]))
                            ])
        ])


#CALLBACK FUNCTION FOR GRAPH
@app.callback(
Output(component_id='output_graph', component_property='children'),
[Input(component_id='input', component_property='value')])
def update_graph(input_data):
    start_date = dt.datetime(2017,1,1)
    end_date = dt.datetime.now()
    input_data = str(input_data).upper()

    #GET REQUEST FOR API
    try:
            name = ticker.loc[input_data, "Company"] 
            df = get_historical_data(str(input_data).upper(),start_date=start_date, end_date=end_date, output_format='pandas')
            
            #CALCULATING PERCENTAGE CHANGE
            pct_changes,COLOR = pct_change_formatter(pct_change(df.close[-2],df.close[-1]))

            #LAYOUT FOR GRAPH
            return (html.Div(className="row", children=[
            html.Div(className="col-lg-8", children=[dcc.Graph(
            id='stocks_graph',
            figure={
            'data':[{'x':df.index, 'y':df.close, 'type':'line', 'name':input_data}],
            'layout':{'title':str(name)}})]),

            #INDICATORS ON SIDE
            html.Div(className="col-lg-4", children=[
            html.Div(className='container top-margin', children=[
            html.Div(className="row", children=[

            #CURRENT PRICE
            html.Div(className="col-sm-8", children=[
            html.H1(className="center-align big-close", children=[df.close[-1]])]),

            #PERCENTAGE CHANGE IN PRICES
            html.Div(className="col-sm-4", children=[
            html.H5(className=COLOR, children=[pct_changes])])]),

            #OPEN PRICE AT THAT DAY
            html.Div(className="row", children=[html.Div(className="col-sm-6", children=[
            html.H6(className="center-align",children=["Open"]), 
            html.H4(className="center-align",children=[df.open[-1]])]),

            #HIGHEST PRICE 
            html.Div(className="col-sm-6", children=[
            html.H6(className="center-align", children=["High"]),
            html.H4(className="center-align",children=[df.high[-1]])])]),

            #LOWEST PRICE
            html.Div(className="row", children=[html.Div(className="col-sm-6", children=[
            html.H6(className="center-align", children=["Low"]), 
            html.H4(className="center-align",children=[df.low[-1]])]),
            
            #VOLUME 
            html.Div(className="col-sm-6", children=[
            html.H6(className="center-align", children=["Volume"]), 
            html.H4(className="center-align",children=[df.volume[-1]])])])])])]))
            
    except:    
            time.sleep(1) 

            
if __name__ == '__main__':
    app.run_server(debug=True)
