FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /kokoc

WORKDIR /kokoc

COPY pyproject.toml poetry.lock ./

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && pip install --upgrade pip poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .
