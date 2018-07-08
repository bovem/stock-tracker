import dash_html_components as html

#LAYOUT FOR INFO PAGE
info_page_layout = html.Div(className='container', 
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
            html.Img(className="col-lg-12 img-margin img-fluid",src="static/images/Untitled.png"),
            html.P(className="lead",
            children=[html.A(html.Button('Try it', className='btn btn-primary btn-lg right-margin'), href='/'), 
            html.A(html.Button('Source Code', className='btn btn-dark btn-lg'), 
            	href='https://github.com/avnish98/stock-tracker', target="_blank")])]),

            #SECOND SECTION
            html.Div(className="container",
            children=[html.H2(className="display-3 top-margin", children=["How I made it?"]),
            html.Hr(className="my-4"), html.H5(children="Data Collection"), html.P(className="lead",
            children=["""I used """,html.A(href="https://github.com/addisonlynch/iexfinance", 
            	children="iexfinance", target="_blank"),""" API for stock data. 
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
            children=["""I used """,html.A(href="https://dash.plot.ly/", children="Dash", target="_blank"),
            """ for Data Visualisation which is a summation of """,
            html.A(href="http://flask.pocoo.org/", children="Flask Framework", target="_blank"), """, """,
            html.A(href="https://plot.ly/", children="Plotly", target="_blank"),""" and """,
            html.A(href="https://reactjs.org/", children="ReactJS", target="_blank"),
            """ for real time update of graph and data."""])
            ]),

            #THIRD SECTION\
            html.Div(className="container", 
            children=[html.H2(className="display-3 top-margin", children="Libraries Used"),
            html.Hr(className="my-4"), html.Ul(className="list-unstyled",
            children=[html.Li("dash"), html.Li("dash_core_components"), html.Li("dash_html_components"), 
            html.Li("iexfinance"), html.Li("pandas"), html.Li("datetime"), html.Li("time")]),
            html.P(className="lead", children=["""Feel free to open a issue at """,
            html.A(href="https://github.com/avnish98/stock-tracker", target="_blank", children="github"),
            """ if you have any problems installing packages
            or the application isn't working on your system."""])])
            
])


