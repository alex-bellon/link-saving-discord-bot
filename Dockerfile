FROM ubuntu:latest

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev
RUN apt-get install -y python3 python3-pip

COPY ./requirements.txt /requirements.txt
COPY ./.env .env

RUN pip3 install -r requirements.txt --upgrade

COPY ./link-saving-discord-bot.py /link-saving-discord-bot.py

CMD ["python3", "link-saving-discord-bot.py"]
