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
pip3 install protobuf


MAINTAINER xhg@servyou
LABEL version=0.6
LABEL description="python image for mlp"
