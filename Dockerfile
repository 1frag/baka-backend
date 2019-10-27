FROM python:3.8

COPY requirements.txt /

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apt-get update -qq \
    && apt install postgresql -y
