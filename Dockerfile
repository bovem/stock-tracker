FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /stock_tracker_app
WORKDIR /stock_tracker_app
ADD . /stock_tracker_app/
RUN python3 -m pip install iexfinance dash_core_components pandas dash dash_renderer dash_html_components
CMD [ "python", "./app.py" ]
