import pika

def on_message_receieved(ch, method, properties, body):

    print(f"receieved new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_receieved)

print("starting consuming")

channel.start_consuming()