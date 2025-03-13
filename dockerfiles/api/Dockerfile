FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    poppler-utils \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /data/tmp /data/storage

WORKDIR /app

ENV PYTHONPATH=/app

COPY app .
COPY resources /resources

RUN pip install --no-cache-dir -r requirements.txt \
    && pip cache purge

EXPOSE 8000

CMD uvicorn app.index:app --host 0.0.0.0 --port ${PORT_API:-8000} --reload
