#! /usr/bin/python3

from os import close, read
import subprocess
from typing import final
import shutil

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


makeBackup(bashrc_path, bkp_path)
try:
    with open(bashrc_path, 'r') as reader, open("outdummy", "w") as writer:
        new_content = ''
        for line in reader:
            if "export ROS_MASTER_URI" in line and line[0] != '#':
                print(line)
            #new_content += line

        writer.write(new_content)

finally:
    reader.close()
    writer.close()

# subprocess.run(["clear"])
# subprocess.run(["bash"])
