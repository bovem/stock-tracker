# Stock Tracker

Stock Tracker is an interactive data visualization application developed in Python, with the help of following libraries:

* [Dash](https://github.com/plotly/dash)  
* [iexfinance](https://github.com/addisonlynch/iexfinance)
* [Pandas](https://github.com/pandas-dev/pandas)

It uses IEX Finance API to get intraday trading data of any NASDAQ listed corporation using the ticker symbol provided and plots it on an interactive graph using Dash. 
 
Other than displaying current price, open price, high, low and volume of that stock, it also calculates percentage change of price in last one day interval. 

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