FROM python:3.8

LABEL maintainer="Rodrigo Eloy Cavalcanti"

COPY . /app

WORKDIR /app

RUN pip install -r ./requirements.txt

CMD python -m api_hoco

EXPOSE 8000