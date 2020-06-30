FROM python:3.7-slim

SHELL ["/bin/bash", "-c"]

COPY ./src/app2/requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "-m", "src.app2.image_watcher"]