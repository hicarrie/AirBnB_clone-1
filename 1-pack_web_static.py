#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from web_static folder
"""


from fabric.api import *
import time


def do_pack():
    """creates .tgz archive from web_static folder"""
    timestr = time.strftime("%Y%m%d%H%M")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except:
        return None
