FROM python:3.11.6-slim-bullseye

ENV \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  libpq-dev \
  wget && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*



COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api_telegram/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./api_telegram/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./api_telegram/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /code

# CMD ["sh", "-c", "celery -A tasks beat; celery -A tasks worker --loglevel=info"]