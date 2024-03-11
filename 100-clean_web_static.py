#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.90.28.121", "54.237.79.178"]

def do_clean(number=0):
    """Deletes out-of-date archives"""
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    number = 1 if number == 0 else int(number)
    for archive in archives[number:]:
        local(f"rm versions/{archive}")
        run(f"rm /data/web_static/releases/{archive}")
