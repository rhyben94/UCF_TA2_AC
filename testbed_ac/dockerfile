FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install dos2unix
RUN apt-get -y install git

COPY ihmc-python-agent-helper-package /ihmc-python-agent-helper-package
COPY requirements.txt /
RUN pip3 install -r requirements.txt --upgrade

ARG CACHE_BREAKER

COPY src/ /app
WORKDIR /app

RUN chmod 777 entrypoint.sh
RUN dos2unix entrypoint.sh
CMD [ "sh","entrypoint.sh"]