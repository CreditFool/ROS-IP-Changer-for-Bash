#!/usr/bin/python3

from os import close, read, write
import subprocess
from typing import final
import shutil
import sys
import re

bashrc_path = "/home/creditfool/kodingan/Project/host swithcer/dummy_bash"
bkp_path = bashrc_path+".bkp"


def makeBackup(source: str, target: str):
    try:
        shutil.copy(source, target)

    except shutil.SameFileError:
        print("There are already file with the same name on target directory")

    except PermissionError:
        print("Permission denied")

    except:
        print("There is error when creating backup file")


def writeMasterURI(address: str):
    return "export ROS_MASTER_URI=http://" + address + ":11311"


def writeHostname(address: str):
    return "export ROS_HOSTNAME=" + address


def readBashrc(path):
    masterIP = ''
    hostIP = ''

    new_content = []
    try:
        with open(path, 'r') as reader:
            for line in reader:
                line_strip = line.strip()
                if "export ROS_MASTER_URI" in line and line[0] != '#':
                    masterIP = line_strip.lstrip(
                        "export ROS_MASTER_URI=http://").rstrip(":11311")

                if "export ROS_HOSTNAME" in line and line[0] != '#':
                    hostIP = line_strip.lstrip("export ROS_HOSTNAME=")

                new_content.append(line_strip)

    finally:
        reader.close()

    return new_content, masterIP, hostIP


def changeHost(path, content, master: str = '', hostname: str = ''):

    MASTER_IP_DEFAULT = "192.168.0.102"
    COMPUTER_IP_DEFAULT = "192.168.0.102"

    try:
        with open(path, "w") as writer:
            for line in content:
                if "export ROS_MASTER_URI" in line and line[0] != '#':
                    if master == '':
                        line = writeMasterURI(
                            (MASTER_IP_DEFAULT if "localhost" in line else "localhost"))
                    else:
                        line = writeMasterURI(master)

                if "export ROS_HOSTNAME" in line and line[0] != '#':
                    if master == '':
                        line = writeHostname(
                            (COMPUTER_IP_DEFAULT if "localhost" in line else "localhost"))
                    else:
                        line = writeHostname(
                            (hostname if (hostname != '') else master))

                writer.write(line+"\n")

    finally:
        writer.close()


def main(args):
    print("Hello, Happy World")


konten, master, host = readBashrc(bashrc_path)
changeHost(bashrc_path, konten)

#makeBackup(bashrc_path, bkp_path)
# args = sys.argv
# masterIP = ''
# hostnameIP = ''

# if len(args) == 1:
#     tes = "httplalal:11311"
#     print(tes.lstrip('http').rstrip(':11311'))
#     print("Happy Lucky Smile Yay")

# elif len(args) == 2:
#     masterIP, hostnameIP = str(args[1])

# elif len(args) >= 3:
#     masterIP = str(args[1])
#     hostnameIP = str(args[2])

# print("ROS IP Configuration will be change to:")
# print("Master: http://"+masterIP+":11311")
# print("HOST: "+masterIP)
# choice = input("continue y/n: ")

# changeHost(bashrc_path)
# subprocess.run(["clear"])
# subprocess.run(["bash"])
