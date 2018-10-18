FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3
CMD mkdir app && cd app
ADD . .
CMD python3 knope.py