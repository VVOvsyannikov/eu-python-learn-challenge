FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIPX_HOME=/opt/pipx \
    PIPX_BIN_DIR=/opt/pipx/bin \
    PATH="/opt/pipx/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        make \
        bash \
        python3-venv \
        python3-pip \
        ca-certificates

RUN pip install --no-cache-dir pipx \
    && pipx ensurepath

RUN pipx install poetry

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install  --no-interaction --no-ansi --no-root

ADD . /app

CMD bash
