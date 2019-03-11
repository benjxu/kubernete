FROM python:3

ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME

ADD https://github.com/benjxu/kubernete/raw/master/instantclient-basiclite-linux.x64-11.2.0.4.0.zip /

RUN \
apt-get update -y && \
apt-get install -y unzip python3-pip libaio1  && \
rm -rf /var/lib/apt/lists/* && \
mkdir -p /opt/oracle && \
unzip "/instantclient*.zip" -d /opt/oracle && \
ln -s $ORACLE_HOME/libclntsh.so.11.1 $ORACLE_HOME/libclntsh.so && \
pip3 install pandas && \
pip3 install pymysql && \
pip3 install SQLAlchemy && \
pip3 install xgboost && \
pip3 install sklearn && \
pip3 install flask && \
pip3 install flask-restplus && \
pip3 install tornado && \
pip3 install elasticsearch && \
pip3 install cx_Oracle && \
pip3 install protobuf && \
pip3 install prometheus_client


MAINTAINER xhg@servyou
LABEL version=1.4
LABEL description="python image for mlp"
