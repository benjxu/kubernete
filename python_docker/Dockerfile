FROM python:3

COPY . /

RUN \
apt-get update -y && \
apt-get install python3-pip -y && \
pip3 install pandas && \
pip3 install pymysql && \
pip3 install SQLAlchemy

CMD ["python", "./read_df.py"]

MAINTAINER xhg@servyou
LABEL version=0.1
LABEL description="python image for mlp"
