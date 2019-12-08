FROM python:3.7
ENV PYTHONUBUFFERED 1
ENV DONTWRITEBYTECODE 1

RUN mkdir /src
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD sh init.sh && python3 manage.py runserver 0.0.0.0:8000
