#!/usr/bin/python3
"""generates a .tgz archive"""
from fabric.api import local
from datetime import datetime



def do_pack():
    """contents of the web_static"""
    f = datetime.now()

    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        f.year, f.month, f.day, f.hour, f.minute, f.second)

    local('mkdir -p versions')
    result = local('tar -cvf versions/{} web_static'.format(file_name))
    print("Packing web_static to versions/{}".format(file_name))

    if result == 0:
        return "versions/{}".format(file_name)
    return None
