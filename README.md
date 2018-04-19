# docker-kafka-cassandra-bridge
A simple yet powerful Kafka 2 Cassandra Bridge

Install

Cassandra cluster, 3 nodes '10.0.0.1','10.0.0.2','10.0.0.3'

Cassandra Keyspace kafka, eg:

CREATE KEYSPACE kafka
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'dc1' : 3 
  };

Kafka 1 broker IP 10.0.0.5 port 32777
