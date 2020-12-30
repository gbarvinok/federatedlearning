FROM hivecell/pysyft:latest

RUN mkdir /app
WORKDIR /app

COPY requirements.txt entrypoint.sh /app/
COPY /src /app/src

RUN pip3 install -r requirements.txt 

WORKDIR /app/

ENTRYPOINT ["sh", "entrypoint.sh"]
