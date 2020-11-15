#©ItzSjDude 
FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt upgrade -y && apt-get install sudo -y
COPY pika.sh /tmp/pika.sh
WORKDIR root/ItzSjDude
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
