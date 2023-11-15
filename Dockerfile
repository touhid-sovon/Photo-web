# Pull the base image
FROM python:3.11.5-slim-bullseye

# set the environment varaibles
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the directory
WORKDIR /code

# install the dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .