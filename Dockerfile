# import the base image
FROM python:3.7

#set  the env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the workdir

WORKDIR /code

#install dependencies
COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

#copy the project

COPY . /code/
