#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive to web servers using the function deploy
"""
from fabric.api import local, task
from os.path import exists

@task
def deploy():
    """The function creates and distributes an archive to web servers"""
    archive_path = local("fab -f 1-pack_web_static.py do_pack", capture=True)
    
    if not archive_path or not exists(archive_path):
        return False

    return local("fab -f 2-do_deploy_web_static.py do_deploy:archive_path={}".format(archive_path), capture=True)
