FROM nvidia/cuda:9.0-base-ubuntu16.04

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cuda-command-line-tools-9-0 \
        cuda-cublas-9-0 \
        cuda-cufft-9-0 \
        cuda-curand-9-0 \
        cuda-cusolver-9-0 \
        cuda-cusparse-9-0 \
        libcudnn7=7.2.1.38-1+cuda9.0 \
        libnccl2=2.2.13-1+cuda9.0 \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        software-properties-common \
				libaio1 \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
        apt-get install nvinfer-runtime-trt-repo-ubuntu1604-4.0.1-ga-cuda9.0 && \
        apt-get update && \
        apt-get install libnvinfer4=4.1.2-1+cuda9.0

ARG USE_PYTHON_3_NOT_2=True
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}
ARG TF_PACKAGE=tensorflow-gpu

ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME

COPY bashrc /etc/bash.bashrc
ADD https://github.com/benjxu/kubernete/raw/master/instantclient-basiclite-linux.x64-11.2.0.4.0.zip /
RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip && \
	${PIP} install --upgrade \
    pip \
    setuptools

RUN \
chmod a+rwx /etc/bash.bashrc && \
mkdir -p /opt/oracle && \
ln -s /usr/bin/python3 /usr/bin/python && \
unzip "/instantclient*.zip" -d /opt/oracle && \
ln -s $ORACLE_HOME/libclntsh.so.11.1 $ORACLE_HOME/libclntsh.so && \
${PIP} install ${TF_PACKAGE}==1.8.0 && \
${PIP} install tensorflow && \
${PIP} install pandas && \
${PIP} install pymysql && \
${PIP} install SQLAlchemy && \
${PIP} install xgboost && \
${PIP} install sklearn && \
${PIP} install flask && \
${PIP} install flask-restplus && \
${PIP} install tornado && \
${PIP} install elasticsearch && \
${PIP} install cx_Oracle && \
${PIP} install protobuf && \
${PIP} install prometheus_client && \
${PIP} install jieba && \
${PIP} install lightgbm && \
${PIP} install jupyter notebook && \
${PIP} install kafka-python && \
${PIP} install python-Levenshtein && \
${PIP} install torch torchvision && \
${PIP} install xlrd && \
${PIP} install pyodps

RUN apt-get clean 

MAINTAINER xhg@servyou.com.cn
LABEL version=2.0
LABEL description="python image for mlp"