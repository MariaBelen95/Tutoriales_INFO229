FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /publisher

COPY ./publisher.py /publisher.py

CMD [ "python", "/publisher.py" ]
