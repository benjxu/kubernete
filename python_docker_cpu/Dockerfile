FROM ubuntu:16.04

ARG USE_PYTHON_3_NOT_2=True
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}
ARG TF_PACKAGE=tensorflow

ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME

ADD https://github.com/benjxu/kubernete/raw/master/instantclient-basiclite-linux.x64-11.2.0.4.0.zip /
RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip && \
	${PIP} install --upgrade \
    pip \
    setuptools

RUN \
mkdir -p /opt/oracle && \
ln -s /usr/bin/python3 /usr/bin/python && \
unzip "/instantclient*.zip" -d /opt/oracle && \
ln -s $ORACLE_HOME/libclntsh.so.11.1 $ORACLE_HOME/libclntsh.so && \
${PIP} install ${TF_PACKAGE}==1.8.0 && \
${PIP} install pandas && \
${PIP} install pymysql && \
${PIP} install SQLAlchemy && \
${PIP} install xgboost && \
${PIP} install sklearn && \
${PIP} install flask && \
${PIP} install flask-restplus && \
${PIP} install tornado && \
${PIP} install "elasticsearch>=6.0.0,<7.0.0" && \
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
${PIP} install lime && \
${PIP} install requests && \
${PIP} install pyodps

RUN apt-get clean 

MAINTAINER xhg@servyou.com.cn
LABEL version=3.0
LABEL description="python image cpu version"