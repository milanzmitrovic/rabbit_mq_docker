
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


# 2. Whenever message is received, this function should be called
def callback_function(ch, method, properties, body):

    print(" [x] Received %r" % body, '----------------- body')
    print(" [x] Received %r" % properties, '----------------- properties')
    print(" [x] Received %r" % method, '----------------- method')
    print(" [x] Received %r" % ch, '----------------- ch')
    print(123)


# 3. Telling RabbitMQ that this particular function should receive message from queue
channel.basic_consume(

    queue='test_queue',
    on_message_callback=callback_function,
    auto_ack=True
)


if __name__ == '__main__':
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

