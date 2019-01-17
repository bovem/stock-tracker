# Stock Tracker

Stock Tracker is an interactive data visualization application developed in Python, with the help of [Dash](https://github.com/plotly/dash) ,                   [iexfinance](https://github.com/addisonlynch/iexfinance) and [Pandas](https://github.com/pandas-dev/pandas)

<img style=" display: block;
     max-width: 100%;
    height: auto;
    margin: auto;
    float: none!important;" src="demo/demo.gif">  

It uses [IEX Finance API](https://iextrading.com/developer/) to get intraday trading data of any [NASDAQ](https://www.nasdaq.com/) listed company.  

It takes the ticker symbol of that company as input and price fluctuations from January 1, 2015 to current date are plotted on an interactive graph provided by plot.ly.

Other than displaying current price, open price, high, low and volume of that stock, it also calculates percentage change of price in the last one-day interval.  

The interface is created using [Litera](https://bootswatch.com/litera/), a bootstrap theme from [Bootswatch](https://bootswatch.com/litera/).

## Installation and Usage

**Microsoft Windows users** have to follow [these](/WININSTALL.md) steps (if Python and Pip are not installed on system)


1. Cloning repository
```bash
git clone https://github.com/avnish98/stock-tracker && cd stock-tracker/
```  

2. Installing dependencies using [pip](https://pip.pypa.io/en/stable/).




```bash
python3 -m pip install -r requirements.txt
```  


3. Executing application 

```bash
python3 app.py
``` 
This command will execute the application in your browser at [http://127.0.0.1:8050/](http://127.0.0.1:8050/)



## Roadmap

Development of a prediction model is still in progress. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)