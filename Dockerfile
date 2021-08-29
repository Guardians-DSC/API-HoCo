FROM python:3.8-slim as dependency

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt


FROM python:3.8-slim

WORKDIR /app

COPY ./api_hoco ./api_hoco

COPY ./tests ./tests

EXPOSE 8000

COPY --from=dependency /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

CMD python -m api_hoco
