#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ['34.74.23.57', '35.196.161.89']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successfully generated, None otherwise.
    """
    datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(datetime_str)
    
    # Create versions directory if it doesn't exist
    local('mkdir -p versions')
    
    # Check if web_static directory exists
    if not os.path.exists('web_static'):
        return None
    
    try:
        # Create the archive
        result = local('tar -cvzf versions/{} web_static'.format(file_name), capture=True)
        if result.succeeded:
            archive_path = "versions/{}".format(file_name)
            print("web_static packed: {} -> {}Bytes".format(archive_path, os.path.getsize(archive_path)))
            return archive_path
        else:
            return None
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path: Path to the archive file to deploy

    Returns:
        True if all operations succeed, False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        True if deployment succeeds, False otherwise
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
