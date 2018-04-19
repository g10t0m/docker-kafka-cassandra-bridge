# docker kafka 2 cassandra bridge
A simple yet powerful Kafka 2 Cassandra Bridge

## Requirements

docker installed on linux

In this example, we will use a Cassandra cluster, 3 nodes '10.0.0.1','10.0.0.2','10.0.0.3'

Cassandra Keyspace kafka, eg:

`CREATE KEYSPACE kafka
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'dc1' : 3 
  };`
  
  use kafka;
  
 CREATE TABLE kafka.telemetry (
    topic text,
    event_time timestamp,
    valore text,
    PRIMARY KEY (topic, event_time)
) WITH CLUSTERING ORDER BY (event_time ASC)

Kafka 1 broker eg: IP 10.0.0.5 port 32777 topic to get data: topic2put

## Install

`mkdir /opt/k-c`

`cd /k-c`

put files here (Dockerfile and Kafka2Cassandra.py)

`docker build -t k-c .`

## Run

`docker run -d --restart-always --name my-k-c k-c`

## Swarm mode

`docker service create --name s-k-c --replicas 1 k-c`

**Note**:

--replicas 1 # i want only one of these in the cluster running


