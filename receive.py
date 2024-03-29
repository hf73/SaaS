import pika, sys, os

credentials = pika.PlainCredentials(username='john', password='123', erase_on_connect=True)
parameters = pika.ConnectionParameters(host='10.147.18.198', port=5672, virtual_host='last', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def main():
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
