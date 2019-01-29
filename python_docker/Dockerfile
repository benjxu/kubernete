FROM python:3

RUN \
apt-get update -y && \
apt-get install python3-pip -y && \
pip3 install pandas && \
pip3 install pymysql && \
pip3 install SQLAlchemy && \
pip3 install xgboost && \
pip3 install sklearn && \
pip3 install flask && \
pip3 install flask-restplus && \
pip3 install tornado && \
pip3 install protobuf && \
pip3 install tensorflow==1.12.0 && \
pip3 install tensorflow-gpu==1.12.0 && \
pip3 install elasticsearch


MAINTAINER xhg@servyou
LABEL version=0.8
LABEL description="python image for mlp"
