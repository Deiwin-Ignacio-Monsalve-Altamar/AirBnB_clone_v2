#!/usr/bin/python3
"""that distributes an archive"""
from fabric.api import local, put, env, run
from datetime import datetime
from os import path, stat

env.hosts = ['35.196.97.61', '34.75.200.40']


def do_pack():
    n = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month, n.day,
                                                    n.hour, n.minute, n.second)
    local("mkdir -p versions")
    path = local("tar -cvzf versions/{} web_static".format(filename))
    print("web_static packed: versions/{} -> {}"
          .format(filename, stat('versions/' + filename).st_size))

    return "versions/{}".format(filename)


def do_deploy(archive_path):
    """Script distributes an archive"""
    if not path.exists(archive_path):
        return False

    try:
        archive_file = archive_path.split('/')[1]
        file_no_ext = archive_file.split('.')[0]
        releases = '/data/web_static/releases/versions/{}/'.format(file_no_ext)
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(releases))
        run('sudo tar -xvf /tmp/{} -C {}'.format(archive_file, releases))
        run('sudo rm /tmp/{}'.format(archive_file))
        run('sudo mv {}/web_static/* {}'.format(releases, releases))
        run('sudo rm -rf {}/web_static'.format(releases))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(releases))
        return True
    except Exception as e:
        return False


def deploy():
    """Extraer function"""
    try:
        archive_path = do_pack()
        value = do_deploy(archive_path)
        return value
    except BaseException:
        return False
