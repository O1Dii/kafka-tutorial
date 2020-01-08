from time import sleep

from kafka import KafkaProducer

# producer part
producer = KafkaProducer(value_serializer=lambda x: x.encode('utf-8'))

for num in range(1000):
    producer.send('nums', value=str(num))
    sleep(3)

