#!/usr/bin/env python2.7

#pip install kafka-python
#pip install cassandra-driver

import time
import datetime
from cassandra.cluster import Cluster
cluster = Cluster(['10.0.0.1','10.0.0.2','10.0.0.3'])
session = cluster.connect('kafka')

print('Bridge Kafka Cassandra wrote in Python')
from kafka import KafkaConsumer
consumer = KafkaConsumer('topic2put',bootstrap_servers='10.0.0.5:32777')
for msg in consumer:
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print (st + ':'+ msg.value)
        session.execute("insert into kafka.telemetry (topic, event_time,valore) values('topic2put',toTimestamp(now()),'"+msg.value+"') using ttl 20;")
