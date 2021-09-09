FROM python:3.9.1
ADD . /flask
WORKDIR /flask
RUN pip install -r requirements.txt