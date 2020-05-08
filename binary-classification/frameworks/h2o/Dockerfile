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
RUN pip --no-cache-dir install -r requirements.txt
RUN pip install distributed==2.10.0 && \
    pip install seaborn python-dateutil dask && \
    pip install pyyaml joblib pytagcloud husl geopy ml_metrics mne pyshp && \
    # Install h2o from source.
    # Use `conda install -c h2oai h2o` once Python 3.7 version is released to conda.
    apt-get install -y default-jre-headless && \
    pip install -f https://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o