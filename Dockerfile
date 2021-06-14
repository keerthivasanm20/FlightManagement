FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

#WE NEED TO MENTION DJANGO ALSO TO BE INSTALLED 
#WE NEED A SERVER TO SO GUNICORN

COPY  ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
