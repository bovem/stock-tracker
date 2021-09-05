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
#RUN cp ../requirements.txt ${workdir}
COPY . app/
RUN python3 -m pip install -r app/requirements.txt
EXPOSE 8050