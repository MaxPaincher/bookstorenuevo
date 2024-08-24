# base image
FROM python:3.12.4-slim-bullseye

# set environments variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONNUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .