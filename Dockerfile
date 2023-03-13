FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT python -m main