#!/usr/bin/python3
from fabric.api import local
from datetime import datetime



def do_pack():
    f = datetime.now()

    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        f.year, f.month, f.day, f.hour, f.minute, f.second)

    local('mkdir -p versions')
    local('tar -cvf versions/{} web_static'.format(file_name))
    print("Packing web_static to versions/{}".format(file_name))

    return "versions/{}".format(file_name)
