FROM python:3.8

EXPOSE 5000

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app
RUN python3 -m pip install -r requirements.txt

ADD . /usr/src/app

ENTRYPOINT ["./entrypoint.sh"]
