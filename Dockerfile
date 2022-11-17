FROM python:3.10.6

WORKDIR /app

COPY . /app

RUN apt-get update -y

RUN apt-get -y install python3-pip ffmpeg libsm6 libxext6

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python server.py