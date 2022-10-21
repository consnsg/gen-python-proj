#!/usr/bin/python python3.10

import os

anime = input("Anime name: ")
season = int(input("Season: "))

dir = f"/home/cloud_user/{anime}"
f = []
for (dirpath, dirnames, filenames) in os.walk(dir):
    f.extend(filenames)
    break

print(f"There are {f.count()} files in this directory.")