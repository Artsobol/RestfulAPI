FROM python:3.12.0-slim

ENV HOME=/home/fast \
    APP_HOME=/home/fast/app \
    PYTHONPATH="$PYTHONPATH:/home/fast" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir -p $APP_HOME \
 && groupadd -r fast\
 && useradd -r -g fast fast


WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt  \
 && rm -rf ~/.cache/pip

COPY app app
COPY alembic.ini .

RUN chown -R fast:fast .

USER fast