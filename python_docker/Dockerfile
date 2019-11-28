FROM nvidia/cuda:9.0-base-ubuntu16.04
ENV DEBIAN_FRONTEND=noninteractive
ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME
# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cuda-command-line-tools-9-0 \
        cuda-cublas-9-0 \
        cuda-cufft-9-0 \
        cuda-curand-9-0 \
        cuda-cusolver-9-0 \
        cuda-cusparse-9-0 \
		libsasl2-dev \
		libsasl2-modules \
		libsasl2-2 \
		krb5-user \
		libsasl2-modules-gssapi-mit \
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


ADD https://github.com/benjxu/kubernete/raw/master/instantclient-basiclite-linux.x64-11.2.0.4.0.zip /
ADD https://github.com/cdr/code-server/releases/download/1.1156-vsc1.33.1/code-server1.1156-vsc1.33.1-linux-x64.tar.gz /
RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip && \
	${PIP} install --upgrade \
    pip \
    setuptools

RUN \
mkdir -p /opt/oracle && \
mkdir -p /opt/code-server && \
ln -s /usr/bin/python3 /usr/bin/python && \
unzip "/instantclient*.zip" -d /opt/oracle && \
tar -zxf /code-server*.tar.gz -C /opt/code-server && \
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
${PIP} install jieba && \
${PIP} install sasl thrift pyhive thrift_sasl && \
${PIP} install redis && \
${PIP} install uwsgi && \
${PIP} install keras && \
${PIP} install skater && \
${PIP} install dill && \
${PIP} install xlwt && \
${PIP} install openpyxl && \
${PIP} install jupyterlab && \
${PIP} install pyodps && \
${PIP} install redis-py-cluster && \
${PIP} install psycopg2-binary && \
${PIP} install catboost

RUN apt-get clean 

LABEL version=2.0
LABEL description="python image for mlp"
