FROM python:3.10-alpine
WORKDIR /usr/src/flask_app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
