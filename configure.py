import os
import venv
import subprocess

os.chdir('admin')
if not os.path.isdir('/venv'):
    venv.create('./venv', with_pip=True)

os.system('venv\\Scripts\\activate.bat & '
          'pip install -r requirements.txt --upgrade & '
          'pyinstaller --onefile --icon "gui/img/logo.ico" --add-data "gui;." daunRat_admin.py')

os.chdir('../client')
if not os.path.isdir('/venv'):
    venv.create('./venv', with_pip=True)

os.system('venv\\Scripts\\activate.bat & '
          'pip install -r requirements.txt --upgrade')

os.chdir('../')


if input("Create admin shortcut? [y/n] ") == 'y':
    with open('shortcut.vbs', 'w+') as f:
        f.write(f'''
Set oWS = WScript.CreateObject("WScript.Shell")
user=oWS.ExpandEnvironmentStrings("%USERPROFILE%")
sLinkFile = user & "\Desktop\daunRat_admin.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{os.getcwd()}/admin/dist/daunRat_admin.exe"
oLink.WorkingDirectory = "{os.getcwd()}/admin/dist"
oLink.Save
    ''')
    subprocess.call('cscript /nologo shortcut.vbs')
    os.remove('shortcut.vbs')

if input("Create builder shortcut? [y/n] ") == 'y':
    with open('shortcut.vbs', 'w+') as f:
        f.write(f'''
Set oWS = WScript.CreateObject("WScript.Shell")
user=oWS.ExpandEnvironmentStrings("%USERPROFILE%")
sLinkFile = user & "\Desktop\daunRat_builder.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{os.getcwd()}/client/venv/Scripts/python.exe"
oLink.Arguments = "{os.getcwd()}/client/builder.py"
oLink.WorkingDirectory = "{os.getcwd()}/client"
oLink.IconLocation = "{os.getcwd()}/admin/gui/img/logo.ico"
oLink.Save
    ''')
    subprocess.call('cscript /nologo shortcut.vbs')
    os.remove('shortcut.vbs')
