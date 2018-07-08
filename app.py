from iexfinance import get_historical_data, Stock
import pandas as pd
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time

app = dash.Dash()

#FOR FETCHING COMPANY NAME FROM TICKER SYMBOL
ticker = pd.read_csv('tickers.csv', index_col="Symbol")

#HTML Layout
app.layout = html.Div(children=[
             #ADDRESS BAR
             dcc.Location(id='url', refresh=False),

             #NAVIGATION BAR
             html.Div(className="container", 
                     children=[html.Nav(className=["navbar navbar-expand-lg navbar-light bg-light"],
                     children=[html.A(className='navbar-brand', href="/",
                     children=["""Stock Tracker"""]),html.Div( className="collapse navbar-collapse",id="navbarColor03",
                     children=[html.Ul(className="navbar-nav mr-auto", 
                     children=[html.Li(className='nav-item', 
                     children=[html.A(className="nav-link", href="/info", 
                     children="""Info""")])])])])]),html.Div(id='page-content') 
            ])

#STYLESHEETS    
app.css.append_css({"external_url": '/static/bootswatch.css'})
app.css.append_css({"external_url": '/static/styles.css'})

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

    #INFO PAGE
    elif pathname == "/info":

        return html.Div(className='container', 
            children=[html.Hr(className="seperator"), 

            #FIRST SECTION
            html.Div(className='container',
            children=[html.H2(className="display-3", children="How it works?"),
            html.Hr(className="my-4"), html.P(className="lead", 
            children=["""Stock tracker is a web application for fetching data of a 
            NASDAQ listed company using ticker symbol. It uses iexfinance API for fetching
             data and Dash, a data visualistion framework by plot.ly"""]), html.P(className="lead",
            children=["""Enter any ticker symbol for a NASDAQ listed company (such as "AAPL" or "GOOGL" 
            or "MSFT") and data is displayed in realtime alongiwth Graph."""]),
            html.Img(className="col-lg-12 img-margin",src="static/images/Untitled.png"),
            html.P(className="lead",
            children=[html.A(html.Button('Try it', className='btn btn-primary btn-lg right-margin'), href='/'), 
            html.A(html.Button('Source Code', className='btn btn-secondary btn-lg'), href='/')])]),

            #SECOND SECTION
            html.Div(className="container",
            children=[html.H2(className="display-3 top-margin", children=["How I made it?"]),
            html.Hr(className="my-4"), html.H5(children="Data Collection"), html.P(className="lead",
            children=["""I used """,html.A(href="/", children="iexfinance"),""" API for stock data. 
            It provides per day data including Open price, Close price,High & Low values and Volume 
            of the stock."""]),

            html.H5(children="Exploratory Data Analysis"),
            html.P(className="lead",
            children=["""  From the data provided by API(open, close, high, low and volume), 
            I calculated Percentage change using formula. """]),
            html.P(className="lead",
            children=[html.Code("""Percentage Change = ((Current Price - Open Price)/Open Price)x100""")]),
            html.P(className="lead", 
            children=[""" I used a "ticker.csv" file for fetching name of the company from its ticker symbol."""]),

            html.H5(children="Data Visualistion"),
            html.P(className="lead",
            children=["""I used """,html.A(href="/", children="Dash"),""" for Data Visualisation which 
            is a summation of """,html.A(href="/", children="Flask Framework"), """, """,
            html.A(href="/", children="Plotly"),""" and """,
            html.A(href="/", children="ReactJS"),""" for real time update of graph and data."""])
            ]),

            #THIRD SECTION\
            html.Div(className="container", 
            children=[html.H2(className="display-3 top-margin", children="Libraries Used"),
            html.Hr(className="my-4"), html.Ul(className="lib-list",
            children=[html.Li("dash"), html.Li("dash_core_components"), html.Li("dash_html_components"), 
            html.Li("iexfinance"), html.Li("pandas"), html.Li("datetime"), html.Li("time")]),
            html.P(className="lead", children=["""Feel free to open a issue at """,
            html.A(href="/", children="github"),""" if you have any problems installing packages
            or the application isn't working on your system."""])])
            
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
            tick = Stock(input_data)

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
