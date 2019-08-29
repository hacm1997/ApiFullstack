FROM python:3.7.3
#imagen base
FROM alpine:3.5

MAINTAINER Heiner Acosta

#Instala python - pip
RUN apk add --update py-pip

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]