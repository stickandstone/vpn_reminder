# pull official base image
FROM python:3.11-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the environment variables to the values in the .env file
# install dependencies
ADD requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


## copy project
COPY . .
ENTRYPOINT python -m main
