# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install wheel

COPY requirements.txt .
RUN pip install -r requirements.txt

## copy project
COPY . .
ENTRYPOINT python -m main
