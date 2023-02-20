FROM python:3.9-alpine3.16

ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

COPY poetry.lock pyproject.toml ./
COPY service /service

WORKDIR /service


EXPOSE 8000

RUN python -m pip install poetry
RUN poetry install

RUN adduser --disabled-password service-user

USER service-user

CMD [ "poetry", "run", "python", "-c", "print('Hello, World!')" ]