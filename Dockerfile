FROM python:3.6

LABEL maintainer="hichtakk@gmail.com"
LABEL version="0.1.0"
LABEL description="Prometheus exporter for Nature Remo E Cloud API."

RUN mkdir /app

COPY nature-remo-e.py /app
COPY pyproject.toml /app

WORKDIR /app

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

ENV CLOUD_API_TOKEN=""
EXPOSE 18001

CMD ["sh", "-c", "/app/nature-remo-e.py --token $CLOUD_API_TOKEN"]