#!/usr/bin/python3
"""that distributes an archive"""
from fabric.api import local, put, env, run
from datetime import datetime
from os import path, stat

env.hosts = ['35.196.97.61', '34.75.200.40']


def do_deploy(archive_path):
    """Script distributes an archive"""
    if not path.exists(archive_path):
        return False

    archive_file = archive_path.split('/')[1]
    file_no_ext = archive_file.split('.')[0]
    releases = '/data/web_static/releases/{}/'.format(file_no_ext)

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(releases))
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, releases))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {}/web_static/* {}'.format(releases, releases))
        run('rm -rf {}/web_static'.format(releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases))
        return True
    except Exception as e:
        return False
