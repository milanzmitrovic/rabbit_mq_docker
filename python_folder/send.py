

# https://www.cloudiqtech.com/rabbitmq-an-open-source-message-broker/

import pika


# 1. Establish a connection to RabbitMQ server

credentials = pika.PlainCredentials(username='myuser',
                                    password='mypassword'
                                    )

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5674,
        credentials=credentials
    )
)

channel = connection.channel()


# 2. Create queue to which messages will be delivered
channel.queue_declare(queue='test_queue')


# 3. Publishing message to queue

# https://github.com/pika/pika/issues/1324
# If RabbitMQ is running low on memory (required hardware should be seen in the bottom of overview page),
# then messages will not be sent from producer to RabbitMQ server.
# But, consumers will be able to consume messages i.e. RabbitMQ server will be sending data to consumers.

# If we are running low on hardware resources, we can send message via RabbitMQ UI.

channel.basic_publish(
    exchange='',
    routing_key='routing_key_test',
    body='test test test'
)

print(" [x] Sent 'Hello RabbitMQ!'")

connection.close()

