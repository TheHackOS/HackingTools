FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
 
COPY requirements.txt ./
 
RUN pip3 install --no-cache-dir -r requirements.txt
 
COPY . .