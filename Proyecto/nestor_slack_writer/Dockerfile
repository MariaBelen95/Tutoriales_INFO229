FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1443019216432-1419428724371-lyxxnv2gVkKilASm60hqDvqh"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
