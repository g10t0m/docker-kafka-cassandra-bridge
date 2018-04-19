FROM python:2

WORKDIR /usr/src/app


RUN pip install --upgrade pip
RUN pip install cassandra-driver
RUN pip install kafka-python

COPY . .

CMD [ "python", "./Kafka2Cassandra.py" ]
