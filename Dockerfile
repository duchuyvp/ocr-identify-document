FROM python:3.8.10

LABEL MAINTAINER="ndh, lvt, bkd"

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update -y

RUN apt-get -y install python3-pip ffmpeg libsm6 libxext6

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python server.py