FROM python:3
ADD app.py tickers.csv /
RUN python3 -m pip install iexfinance dash_core_components pandas dash dash_renderer dash_html_components
CMD [ "python", "./app.py" ]
