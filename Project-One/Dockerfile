FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       pkg-config \
       default-libmysqlclient-dev \
    && pip install --no-cache-dir flask mysqlclient \
    && apt-get purge -y gcc pkg-config \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 5002
CMD ["python", "app.py"]
