FROM python:3.8-buster
ENV PYTHONUBUFFERED 1
ENV DONTWRITEBYTECODE 1
RUN mkdir /app
RUN apt-get update && apt-get install -y curl && apt-get install
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD ./ /app


