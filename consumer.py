from kafka import KafkaConsumer

# consumer
consumer = KafkaConsumer('nums',
                         auto_offset_reset='earliest',  # 'latest' is default
                         enable_auto_commit=True,  # default
                         group_id='my-group',
                         value_deserializer=lambda x: x.decode('utf-8'))

for message in consumer:
    print(message)
    print(message.value)
