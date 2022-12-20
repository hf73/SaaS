import pika, sys, os
credentials = pika.PlainCredentials(username='john', password='123', erase_on_connect=True)
parameters = pika.ConnectionParameters(host='10.147.18.198', port=5672, virtual_host='last', credentials=credentials)
connection = pika.BlockingConnection(parameters)
from website import create_app #accesses website file to import create_app from __init__

app = create_app()

if __name__ == '__main__': #if file is ran, not when it is imported, then the website gets ran 
    app.run(debug=True, host='0.0.0.0') #anytime a change is done to the code, then the website get rerun (turn off for prod good for dev)

    connection.close()
