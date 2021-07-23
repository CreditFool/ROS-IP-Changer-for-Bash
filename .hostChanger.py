#!/usr/bin/python3

from os import close, read, write
import subprocess
from typing import final
import shutil
import sys


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
    return f"export ROS_MASTER_URI=http://{address}:11311"


def writeHostname(address: str):
    return f"export ROS_HOSTNAME={address}"


def readBashrc(path: str):
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


def changeHost(path: str, content, master: str = '', hostname: str = ''):

    MASTER_IP_DEFAULT = "192.168.0.102"
    COMPUTER_IP_DEFAULT = "192.168.0.102"

    try:
        with open(path, "w") as writer:
            for line in content:
                if "export ROS_MASTER_URI" in line and line[0] != '#':
                    if master == '':
                        line = writeMasterURI(
                            (MASTER_IP_DEFAULT if "localhost" in line else "localhost")
                        )
                    else:
                        line = writeMasterURI(master)

                if "export ROS_HOSTNAME" in line and line[0] != '#':
                    if master == '':
                        line = writeHostname(
                            (COMPUTER_IP_DEFAULT if "localhost" in line else "localhost")
                        )
                    else:
                        line = writeHostname(
                            (hostname if (hostname != '') else master)
                        )

                writer.write(line+"\n")

    finally:
        writer.close()


def main(args):
    BASHRC_PATH = "/home/creditfool/kodingan/Project/host swithcer/dummy_bash"
    BACKUP_PATH = BASHRC_PATH + ".backup"

    MASTER_IP_DEFAULT = "192.168.0.102"
    COMPUTER_IP_DEFAULT = "192.168.0.102"

    basrc_content, current_master, current_host = readBashrc(BASHRC_PATH)
    new_master = ''
    new_host = ''
    if len(args) == 1:
        new_master = (
            MASTER_IP_DEFAULT if current_master == "localhost" else "localhost"
        )
        new_host = (
            COMPUTER_IP_DEFAULT if "localhost" in current_host else "localhost"
        )

    elif len(args) == 2:
        new_master = new_host = str(args[1])

    elif len(args) >= 3:
        new_master = str(args[1])
        new_host = str(args[2])

    print("\nROS IP Configuration will be change to:")
    print(
        f"Master: http://{current_master}:11311   =>   http://{new_master}:11311"
    )
    print(f"HOST  : {current_host}                =>   {new_host}")

    choice = input("\ncontinue y/n (default n): ")
    if choice == 'y':
        changeHost(BASHRC_PATH, basrc_content, new_master, new_host)
        subprocess.run(["clear"])
        subprocess.run(["bash"])
    else:
        print("Program Aborted")


main(sys.argv)
