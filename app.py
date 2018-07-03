#import quandl
from iexfinance import get_historical_data, Stock
import pandas_datareader.data as web
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

#HTML Layout
app.layout = html.Div(children=[
            
                html.H1(className='text-center', children="""
                    STOCK TRACKER
                    """),
                #Using bootstrap theme 
		        html.Div(className='container', 
		                children=[html.Div(className ='row', 

                        #Ticker column
                        children=[html.Div(className ='col-lg-4',
                        children=[html.Form(html.Fieldset(
                        children=[html.Div(className ='form-group', 
                        children=[html.Label(children="""TICKER"""),
                        dcc.Input(id='input', className='form-control',value='', type='text')]
                        )]
                        ))]),

                        #Graph column
                        html.Div(className='col-lg-8',
                        children=[html.Div(id='output_graph')])])])


])

app.css.append_css({"external_url": '/static/bootswatch.css'}) #stylesheet used


@app.callback(
Output(component_id='output_graph', component_property='children'),
[Input(component_id='input', component_property='value')]
)

def update_graph(input_data):
    start_date = dt.datetime(2017,1,1)
    end_date = dt.datetime.now()
    #input_data2 = "WIKI/"+input_data

    #Get request for API
    #df = get_historical_data(str(input_data),start_date=start_date, end_date=end_date, output_format='pandas')
    df = Stock(str(input_data))
    
    # Graph layout
    return dcc.Graph(
            id='stocks_graph',
            figure={
            'data':[{'x':end_date, 'y':df.get_close(), 'type':'dot ', 'name':input_data}],
            'layout':{'title':input_data.upper()}})

if __name__ == '__main__':
    app.run_server(debug=True)
