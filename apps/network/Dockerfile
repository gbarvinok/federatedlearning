FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y git python3-pip libffi-dev

COPY requirements.txt entrypoint.sh /app/
COPY /src /app/src

WORKDIR /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
