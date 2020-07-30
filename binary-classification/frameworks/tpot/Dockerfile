FROM python:3.7-buster

RUN mkdir -p /opt/automl

WORKDIR /opt/automl

# Uncomment the following COPY line and the corresponding lines in the `RUN` command if you wish to
# include your requirements in the image itself. It is suggested that you only do this if your
# requirements rarely (if ever) change.
COPY requirements.txt .
#COPY model.py .

# Configure apt and install packages
RUN apt-get update && apt-get install -y \
    && apt-get -y install git iproute2 procps lsb-release
#RUN pip --no-cache-dir install --upgrade git+https://github.com/scikit-learn-contrib/categorical-encoding
RUN pip --no-cache-dir install -r requirements.txt