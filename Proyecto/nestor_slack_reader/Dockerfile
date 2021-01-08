FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1443019216432-1419428724371-ycm4a2lK32ijwJcnw2Cf8hgC"
ENV SLACK_SIGNING_SECRET="9e930243dd3841e48897ff0e42f105af"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader

COPY ./nestor_slack_reader.py /nestor_slack_reader.py

CMD [ "python", "/nestor_slack_reader.py" ]
