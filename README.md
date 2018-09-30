Stock Tracker
==
This is a [Dash](.plot.ly/) server application that uses IEX API to display stock data using ticker symbol of any NASDAQ listed company.

How it works?
--
Enter any ticker symbol for a NASDAQ listed company (such as "AAPL" or "GOOGL" or "MSFT") and data is displayed in real time alongwith Graph.

![Example](static/images/Untitled.png)

Downloading and requirements
--
To download the application
`git clone https://github.com/avnish98/stock-tracker.git && cd stock-tracker`

To install dependencies
`pip install -r requirements.txt`

How I made it?
--
### Data Collection

I used [iexfinance](https://github.com/addisonlynch/iexfinance) API for stock data. It provides per day data including Open price, Close price, High & Low values and Volume of the stock.

### Exploratory Data Analysis

From the data provided by API(open, close, high, low and volume), I calculated Percentage change using formula:

``Percentage Change = ((Current Price - Open Price)/Open Price)x100``

I used a "ticker.csv" file for fetching name of the company from its ticker symbol.

### Data Visualization

I used Dash for Data Visualization which is a summation of [Flask Framework](http://flask.pocoo.org/",), [Plotly](https://plot.ly/) and [ReactJS](https://reactjs.org/) for real time update of graph and data, with changing ticker symbols.

#### Note

Since the html code written through the dash is difficult to understand I have added equivalent HTML code in 
[html/](/html/) folder.

Stylesheet
--
I have used Litera theme from [Bootswatch](https://bootswatch.com/)