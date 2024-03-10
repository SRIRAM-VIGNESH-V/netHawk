import platform,os

machine_os = platform.system()

if machine_os == 'Linux':
    os.system('mkdir /usr/share/netHawk')
    os.system('cp -r * /usr/share/netHawk')
    os.system('ln -s /usr/share/netHawk/netHawk.py /usr/bin/netHawk')
    print('[+] netHawk installed')
elif machine_os == 'Windows':
    os.system("mkdir C:\\netHawk")
    os.system("copy * C:\\netHawk")
    os.system("mkdir C:\\netHawk\\modules")
    os.system("copy modules C:\\netHawk\\modules\\")
    os.system("echo @echo off > C:\\Windows\\System32\\netHawk.bat")
    os.system("echo python3 C:\\netHawk\\netHawk.py %* >> C:\\Windows\\System32\\netHawk.bat")
    print('\n[+] netHawk installed\n')
