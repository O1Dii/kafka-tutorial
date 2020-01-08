from kafka.admin import NewTopic, KafkaAdminClient

admin_client = KafkaAdminClient()

# creating topic via AdminClient
my_topic = NewTopic('nums', 1, 1)
admin_client.create_topics([my_topic])
# validate_only - If True, don’t actually create new topics. Default: False

# # deleting topic via AdminClient
# admin_client.delete_topics(['nums'])
