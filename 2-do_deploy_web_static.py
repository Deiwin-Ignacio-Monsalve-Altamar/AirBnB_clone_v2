#!/usr/bin/python3
"""that distributes an archive"""
from fabric.api import local, env, put, run
from datetime import datetime
from os import path


env.hosts = ['35.196.97.61', '34.75.200.40']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Script distributes an archive"""

    if not path.isfile(archive_path):
        return False

    archive_file = archive_path.split('/')[1]
    name_file = archive_file.split('.tgz')
    release = '/data/web_static/releases/{}'.format(name_file)

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(release))
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, release))
        run('rm -rf /tmp/{}'.format(archive_file))
        run('mv {}//web_static/* {}'.format(release, release))
        run('rm -rf {}/web_static'.format(release))
        
        current_file = '/data/web_static/current'
        run('rm -rf {}'.format(current_file))
        run('ln -sf {} {}'.format(current_file, release))
        return True
    except Exception as e:
        return False

