#!/usr/bin/python3
"""
A Fabric script that distributes an archive to web servers using the function do_deploy
"""
from fabric.api import run, put, env
from os.path import exists

env.hosts = ['52.90.14.176', '100.27.5.123']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """The function deploys an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>/
        archive_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/" + archive_name.split(".")[0]
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, folder_name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Move contents to the current folder
        run("mv {}/web_static/* {}".format(folder_name, folder_name))

        # Remove the empty web_static folder
        run("rm -rf {}/web_static".format(folder_name))

        # Remove the previous symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
