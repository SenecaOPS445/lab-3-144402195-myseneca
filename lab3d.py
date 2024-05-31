#!/usr/bin/env python3

# Author ID: jhyppolite

import subprocess

def free_space():
    result = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell=True, text=True)
    return result.strip()

if __name__ == '__main__':
    print(free_space())

