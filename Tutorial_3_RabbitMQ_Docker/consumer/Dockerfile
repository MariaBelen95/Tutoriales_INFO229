FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /consumer

COPY ./consumer.py /consumer.py

CMD [ "python", "/consumer.py" ]
