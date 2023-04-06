#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
and move it to the servers
"""

from fabric.api import put, env, run
from os.path import exists

env.hosts = ['18.234.192.255', '54.164.58.89']


def do_deploy(archive_path):
    """Deploys the web static to the server"""
    if not exists(archive_path):
        return False

    try:
        archiveWithExt = archive_path.split("/")[-1]
        archiveNoExt = archiveWithExt.split(".")[0]
        releaseVersion = "/data/web_static/releases/{}/".format(archiveNoExt)
        symLink = "/data/web_static/current"

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releaseVersion))
        run("tar -xzf /tmp/{} -C {}".format(archiveWithExt, releaseVersion))
        run("rm -rf /tmp/{}".format(archiveWithExt))
        run("mv {0}web_static/* {0}".format(releaseVersion))
        run("rm -rf {}web_static".format(releaseVersion))
        run("rm -rf {}".format(symLink))
        run("ln -s {} {}".format(releaseVersion, symLink))
        return True
    except:
        return False
