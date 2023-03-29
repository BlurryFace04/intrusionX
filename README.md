# intrusionX
Welcome to intrusionX, a project that showcases the power of Python in the realm of cybersecurity. This repository contains two Python scripts designed to
demonstrate the implementation of a netcat based reverse shell. Dive into the world of secure connections, remote access, and advanced networking techniques. Explore
the intricacies of sockets, subprocesses, and threading as you navigate through this captivating project. Get ready to be amazed by the limitless possibilities that
Python and cybersecurity have to offer!

In this tutorial, we will cover the following topics:

1. Setting up the project environment and required libraries
2. Developing a client-side script to be executed on the victim machine
3. Setting up the tool to run automatically on system startup on victim machine
4. Setup the server
5. Run the scripts on the victim machine
<br>

## Installation
Install the source code:
```
git clone https://github.com/BlurryFace04/intrusionX.git
cd intrusionX
```

Setup virtual environment in Windows (optional):
```
python -m venv venv
call venv\Scripts\activate
```

Setup virtual environment in Linux (optional):
```
python3 -m venv venv
source venv/bin/activate
```

Install libraries:
```
pip install -r requirements.txt
```
<br>

## Client
To prepare the [client script](https://github.com/BlurryFace04/intrusionX/blob/main/client.py) for execution on the target machine, you'll need to convert it into an
executable (.exe) file using PyInstaller. This process makes it easier to run the script on the target system without even requiring a separate Python installation on
the target machine.

Change the Server IP Address and run the following command to convert your [client script](https://github.com/BlurryFace04/intrusionX/blob/main/client.py) into a
standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico client.py
```
**Note:** The [client script](https://github.com/BlurryFace04/intrusionX/blob/main/client.py) provided can only be executed on Windows.
<br><br><br>

## Run script on startup
In order to ensure that the keylogger runs automatically every time the target system starts, you can use the 
[startup script](https://github.com/BlurryFace04/intrusionX/blob/main/startup.py).

Run the following command to convert your [startup script](https://github.com/BlurryFace04/intrusionX/blob/main/startup.py) into a standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico startup.py
```
This will copy the client.exe file to any derired location which can be edited in the [startup script](https://github.com/BlurryFace04/intrusionX/blob/main/startup.py)
and create a shortcut to the client.exe file in the Windows Startup folder, ensuring that the keylogger runs every time the system starts.
<br><br><br>

## Server
To maximize the potential of your intrusionX project, it is strongly advised to consider renting a dedicated/shared server or a virtual private server (VPS) for
running your netcat listener. By opting for a rented server, you can gain remote access and control over your project from any location, eliminating the constraints
imposed by a local area network (LAN) when using a home PC or laptop. This approach significantly enhances the flexibility and reach of your intrusionX project,
enabling more efficient monitoring and management across various network environments.

For this tutorial, we will be using an Ubuntu Server.

If you don't have netcat installed on your Ubuntu Server then install it by executing the following command:
```
sudo apt install netcat
```
Once installed, initiate the netcat listener by executing the following command:
```
nc -lnvp 4242 -s <SERVER_IP>
```
Upon successful execution, netcat will be up and running, actively listening for incoming connections from your client script.
<br><br><br>

## Execution
After generating the executable files, you will find the client.exe and startup.exe files within the dist folder created by PyInstaller.

To deploy intrusionX on the target machine, transfer both files using an appropriate method, such as a USB flash drive, a Rubber Ducky, or another suitable technique.

Once connected to the target system, execute both the executables to initiate the reverse shell process.

### USB Flash Drive:
If using a USB flash drive, simply execute the client.exe and startup.exe files. This will initiate the intrusionX reverse shell and copy the client.exe file to the
pre-defined location on the target system and create a shortcut in the Windows Startup folder, ensuring the reverse shell is launched each time the system starts.

### Rubber Ducky:
You can create a script for Rubber Ducky using the following steps:

1. Use the [payload.txt](https://github.com/BlurryFace04/intrusionX/blob/main/payload.txt) provided in the source code and create a inject.bin (binary payload file)
from [Hak5 PayloadStudio](https://payloadstudio.hak5.org/community/)
2. Copy the inject.bin, client.exe and startup.exe files to the root of the Rubber Ducky's microSD card.
3. Insert the Rubber Ducky into the target system and the payload script will automatically execute both the executables. 
<br>

## Bugs, Issues and Contributing
If you find bugs or have suggestions about improving the module, don't hesitate to contact me.
<br><br><br>

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/BlurryFace04/intrusionX/blob/main/LICENSE) file for details

Copyright (c) 2023 Blurry Face
