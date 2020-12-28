FROM hivecell/pysyft:v0.2.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt entrypoint.sh /app/
COPY /src /app/src

RUN pip3 install -r requirements.txt 

WORKDIR /app/

ENTRYPOINT ["sh", "entrypoint.sh"]
