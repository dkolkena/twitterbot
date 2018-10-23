FROM ubuntu:latest

ENV HOME=/root
WORKDIR $HOME

RUN apt-get update && apt-get install -y \
    python3

RUN mkdir -p $HOME/app && cd $HOME/app
ADD . .
CMD [ "python3", "knope.py" ]
