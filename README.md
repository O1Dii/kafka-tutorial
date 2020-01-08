# Kafka 
We need zookeeper server to be installed to run kafka
#### basic installation:
>sudo apt-get install openjdk-8-jdk
>sudo apt-get install zookeeperd
>systemctl status zookeeper

It should be active. We can manage zookeeper service from now on. We may want to
enable automatic start of zookeeper service :)

Kafka executable can be downloaded from the [website](https://kafka.apache.org/downloads)
(i downloaded the latest scala 2.12 version of kafka)

Then we unpack kafka files to any folder, for example '/opt/kafka'

#### usage:
We need to locate the folder, where kafka is installed ('/opt/kafka' in my case).
To start kafka server we 'cd' in our kafka folder and write
>bin/kafka-server-start.sh config/server.properties

(It asked for sudo, when i did it)  
We can change properties in config/server.properties file


#### documentations:
* [kafka-python documentation](https://kafka-python.readthedocs.io/en/master/index.html)
* [confluent-kafka documentation](https://docs.confluent.io/current/clients/confluent-kafka-python/)

![](./static/fundamentals.jpg)
Kafka is simply a collection of topics split into one or more partitions. 
A Kafka partition is a linearly ordered sequence of messages, where each message is identified by their index (called as offset). 
All the data in a Kafka cluster is the disjointed union of partitions. 
Incoming messages are written at the end of a partition and messages are sequentially read by consumers. 
Durability is provided by replicating messages to different brokers.
Brokers are servers with another kafka started.
[for more information](https://www.tutorialspoint.com/apache_kafka/apache_kafka_fundamentals.htm)

For building large applications, **topics may be divided into partitions**. That
helps to get rid of overload for one broker. **Each partition is a new broker
server.** We define number of partitions when creating topic.
![](./static/partitions.png)
We also define a number of replications for each partition. It can't be set
to one partition, it's shared across partitions of one topic. Replication
factor - number of copies of each partition (usually 3).
![](./static/replication_factor.png)
Group of servers which store the same data is called clusters. Cluster has
the leader partition and following partitions. If the leader partition fails,
the next partition becomes the leader.
![](./static/cluster.png)
[multi-broker cluster example](https://kafka.apache.org/documentation/#quickstart_multibroker)

 
For handling messages consuming, we create multiple consumers, but it
is unclear, which source should consumer read. Consumer groups were created
to handle this problem. When creating a consumer, we define it's consumer
group id and many more. **Consumers in one consumer group can't share a
partition**, thus they can't both parallel read same messages working. You can't 
have more consumers than partitions, extra consumers will read nothing -> be
useless.

>To locate the needed message we need to know the **topic, partition and
 offset.**

Each message has it's offset, it's his number in a queue. Queue doesn't get
deleted after being read, it is stored for some time that you can set yourself
(default - 3 days).

When creating a producer we have different parameters. We can use message
acknowledgement system if loosing data is unacceptable, we can also set the
number of retries and many more




