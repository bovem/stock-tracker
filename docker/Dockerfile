FROM continuumio/anaconda3:2019.03

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
        libpq-dev \
        build-essential \
        git \
        sudo \
        cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev libboost-all-dev libsdl2-dev swig \
        unzip zip python3 python3-pip\
    && rm -rf /var/lib/apt/lists/*

RUN mkdir app/
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install yfinance
EXPOSE 8050