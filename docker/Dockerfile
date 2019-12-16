FROM ubuntu:19.04

RUN echo Version 2

RUN apt update
RUN apt install -y python3-dev
RUN apt install -y python3-pip

RUN pip3 install requests
RUN pip3 install socket-tentacles
RUN pip3 install gributils-annotator>=0.9.0

ADD server.sh /server.sh

CMD ["/server.sh"]
