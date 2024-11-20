# FROM python:3
# ENV PYTHONNUNBUFFERD 1
# RUN mkdir /app
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt
# COPY . /app/
# syntax = docker/dockerfile:1
FROM python:alpine 
# set this env variable to 1 to prevent python from generating cache files
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt

RUN pip install --upgrade pip
  
RUN --mount=type=cache,target=/root/.cache \
	pip install -r requirements.txt

COPY . /home/app