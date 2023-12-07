#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the contents
of web_static folder using the function do_pack
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """The function generates a .tgz file """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

        local("tar -czvf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception:
        return None
