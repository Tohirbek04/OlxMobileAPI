FROM python:3

WORKDIR /app

COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt

COPY /compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY /compose/start /backend-start
RUN sed -i 's/\r$//g' /backend-start
RUN chmod +x /backend-start

COPY /compose/celery/start /celery-start
RUN sed -i 's/\r$//g' /celery-start
RUN chmod +x /celery-start

COPY /compose/celery/beat/start /beat-start
RUN sed -i 's/\r$//g' /beat-start
RUN chmod +x /beat-start

COPY /compose/celery/flower/start /flower-start
RUN sed -i 's/\r$//g' /flower-start
RUN chmod +x /flower-start

