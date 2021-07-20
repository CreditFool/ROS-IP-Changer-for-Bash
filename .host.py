#! /usr/bin/python3

from os import close, read
import subprocess
from typing import final
import shutil
import socket

bashrc_path = "/home/creditfool/kodingan/Project/host swithcer/dummy_bash"
bkp_path = bashrc_path+".bkp"

local = "localhost"
computerIP = "192.168.0.102"
host = socket.gethostbyname(socket.gethostname())
print(host)


def makeBackup(source: str, target: str):
    try:
        shutil.copy(source, target)

    except shutil.SameFileError:
        print("There are already file with the same name on target directory")

    except PermissionError:
        print("Permission denied")

    except:
        print("There is error when creating backup file")


makeBackup(bashrc_path, bkp_path)


def changeHost(path, master, hostname=''):
    try:
        with open(path, 'r') as reader, open("outdummy", "w") as writer:
            new_content = ''
            for line in reader:
                line_strip = line.strip()
                if "export ROS_MASTER_URI" in line and line[0] != '#':
                    line_strip = "export ROS_MASTER_URI=http://"+master+":11311"

                if "export ROS_HOSTNAME" in line and line[0] != '#':
                    line_strip = "export ROS_HOSTNAME=" + \
                        (hostname if (hostname != '') else master)

                new_content += line_strip+"\n"

            writer.write(new_content)

    finally:
        reader.close()
        writer.close()


changeHost(bashrc_path, "192.1.0.0", "192.1.1.1")
# subprocess.run(["clear"])
# subprocess.run(["bash"])
