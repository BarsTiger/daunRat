from env import *
import pusher
import pysher
import sys

client = pusher.Pusher(
    app_id=app_id,
    key=key,
    secret=secret,
    cluster=cluster,
    ssl=False
)
receiver = pysher.Pusher(key=key, cluster=cluster)


def handle_connection_to_server(connection):
    print("Connected to server")
    print("Server returned: " + str(connection))
    ids = dict()

    print("Available client IDs: " +
          str(', '.join(list(map(lambda channel_id: channel_id.split('-')[-1],
                                 list(client.channels_info(prefix_filter='admin-')['channels']))))))
    client_id = input("Enter id to connect: ")
    client.trigger('admin-' + client_id, 'connection_from_admin', None)
    print("Sent connection message to client")
    while True:
        client.trigger('admin-' + client_id, 'command', input("Enter shell command: "))
        print("Sent shell command to client")


if __name__ == '__main__':
    receiver.connection.bind('pusher:connection_established', handle_connection_to_server)
    receiver.connect()
    while True:
        pass
