FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

COPY bot /bot

RUN pip3 install -r /bot/requirements.txt

ENTRYPOINT ["flask"]
WORKDIR /bot
CMD ["run", "--host=0.0.0.0"]
