#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


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
