# Stock Tracker

Stock Tracker is an interactive data visualization application developed in Python, with the help of 

* [Dash](https://github.com/plotly/dash)  
* [iexfinance](https://github.com/addisonlynch/iexfinance)
* [Pandas](https://github.com/pandas-dev/pandas)

It uses [IEX Finance API](https://iextrading.com/developer/) to get intraday trading data of any [NASDAQ](https://www.nasdaq.com/) listed company.  

For that, it takes the ticker symbol of that company as input and price fluctions over a periord of ____ are plotted it on an interactive graph provided by plot.ly. 
 
Other than displaying current price, open price, high, low and volume of that stock, it also calculates percentage change of price in last one day interval. 

The interface is created using [Litera](https://bootswatch.com/litera/), a bootstrap theme from [Bootswatch](https://bootswatch.com/litera/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Roadmap
I am thinking about adding a prediction model to the applicaion.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)