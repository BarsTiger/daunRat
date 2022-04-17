from env import *
import pusher
import pysher

sender = pusher.Pusher(
    app_id=app_id,
    key=key,
    secret=secret,
    cluster=cluster,
    ssl=True
)


def connect_handler(*args):
    print("Connected to server")
    channel = receiver.subscribe('test-doubler-sender')
    print("id=", channel)
    channel.bind('doubler', on_doubler)


receiver = pysher.Pusher(key=key, cluster=cluster)

if __name__ == '__main__':
    print("daunRat by ANONYMUSSSS")
    receiver.connection.bind('pusher:connection_established', connect_handler)
    receiver.connect()
    while True:
        pass
