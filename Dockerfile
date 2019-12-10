FROM python:3.7
ENV PYTHONUBUFFERED 1
ENV DONTWRITEBYTECODE 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD ./ /app
EXPOSE 8000

