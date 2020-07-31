FROM python:3.7-slim-buster

RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gnutls-bin \
        git \
        wget \
        bzip2 \
        curl \
        ca-certificates \
        ninja-build \
        ccache \
        libopenblas-dev \
        libopencv-dev \
        python3-dev \
        gcc \
        cmake && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/
    
RUN git clone -c http.sslverify=false --recursive https://github.com/apache/incubator-mxnet mxnet
WORKDIR mxnet
RUN cp config/linux.cmake config.cmake && \
    mkdir build
WORKDIR build
RUN cmake .. && \
    cmake --build .
RUN pip install -e .
    
RUN mkdir -p /opt/automl

WORKDIR /opt/automl

# Uncomment the following COPY line and the corresponding lines in the `RUN` command if you wish to
# include your requirements in the image itself. It is suggested that you only do this if your
# requirements rarely (if ever) change.
COPY requirements.txt .
#COPY model.py .

# Configure apt and install packages
# RUN apt-get update && apt-get install -y \
#     && apt-get -y install git iproute2 procps lsb-release

#RUN pip install mxnet==1.6.0
RUN pip install autogluon==0.0.12
RUN pip --no-cache-dir install -r requirements.txt
