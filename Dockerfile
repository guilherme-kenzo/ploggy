FROM python:3.8

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 0

# Updating repos
RUN apt-get update
RUN apt-get -y dist-upgrade

# Setting workdir to /code folder
WORKDIR /code

# Installing python and pip
RUN apt-get -y install python-pip
## Installing pipenv
RUN pip3 install pipenv

# Setting up virtual enviroment and fetching pipefile
COPY Pipfile* ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
ENV PATH="/.venv/bin:$PATH"

# Copying code to env
COPY . .

ENTRYPOINT ["/code/docker-entrypoint.sh"]
