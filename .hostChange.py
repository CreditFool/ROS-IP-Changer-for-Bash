#!/usr/bin/python3

from os import close, read
import subprocess
from typing import final
import shutil
import socket
import sys

bashrc_path = "/home/creditfool/kodingan/Project/host swithcer/dummy_bash"
bkp_path = bashrc_path+".bkp"

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


#makeBackup(bashrc_path, bkp_path)


def changeHost(path, master='', hostname=''):

    masterIP_default = "192.168.0.102"
    computerIP_default = "192.168.0.102"

    new_content = ''
    try:
        with open(path, 'r') as reader:
            for line in reader:
                line_strip = line.strip()
                if "export ROS_MASTER_URI" in line and line[0] != '#':
                    if master == '':
                        line_strip = "export ROS_MASTER_URI=http://" + \
                            (masterIP_default if "localhost" in line_strip else "localhost")+":11311"

                    else:
                        line_strip = "export ROS_MASTER_URI=http://"+master+":11311"

                if "export ROS_HOSTNAME" in line and line[0] != '#':
                    if master == '':
                        line_strip = "export ROS_HOSTNAME=" + \
                            (computerIP_default if "localhost" in line_strip else "localhost")

                    else:
                        line_strip = "export ROS_HOSTNAME=" + \
                            (hostname if (hostname != '') else master)

                new_content += line_strip+"\n"

    finally:
        reader.close()

    try:
        with open(path, "w") as writer:
            writer.write(new_content)

    finally:
        writer.close()


changeHost(bashrc_path)
# subprocess.run(["clear"])
# subprocess.run(["bash"])
