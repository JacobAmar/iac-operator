FROM ubuntu:22.04
ARG TERRAFORM_VERSION=1.5.2
RUN apt-get update -y && \
apt-get install -y unzip git wget
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN mv terraform /usr/local/bin/
RUN terraform --version 

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN python3 -V
RUN pip --version

WORKDIR /app
COPY . .