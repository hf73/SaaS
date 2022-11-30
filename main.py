import pika, sys, os
credentials = pika.PlainCredentials(username='danny', password='123', erase_on_connect=True)
parameters = pika.ConnectionParameters(host='10.147.18.152', port=5672, virtual_host='490', credentials=credentials)
connection = pika.BlockingConnection(parameters)
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

connection.close()

    
