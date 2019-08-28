FROM python:3.7.3
#imagen base
FROM alpine:3.5

#Instala python - pip
RUN apk add --update py-pip

#Modulos de python
COPY requirements.txt /ApiFullstack
RUN pip install --no-cache-dir -r requirements.txt

#Copiar archivos requeridos
COPY app.py /ApiFullstack
COPY templates/index.html /templates

#Puerto
EXPOSE 5000

#Ejecutar app
CMD ["Python", "app.py"]