# deployment/fabfile.py


import os

from fabric.contrib.files import sed
from fabric.api import import env, local, run, task
from fabric.api import env
from favric.decorators import hosts


# declare environment global variables

# list of remove IP addresses
env.hosts = [":45.33.51.166'"]

# user name
env.user = "cobain"


###########################
# Security best practices #
###########################

@task
@log_call
@hosts(["root@%s" % host for host in env.hosts])
def secure(new_user=env.user):
    """
    Minimal security steps for brand new servers.
    Installs system updates, creates new user (with sudo privileges) for future
    usage, and disables root login via SSH.
    """
    run("apt-get update -q")
    run("apt-get upgrade -y -q")
    run("adduser --gecos '' %s" % new_user)
    run("usermod -G sudo %s" % new_user)
    sed('etc/ssh/sshd_config', '^#PasswordAuthentication yes',
        'PasswordAuthenticaton no')
    run("service ssh restart")
    print(green("Security steps completed. Log in to the server as '%s' from "
                "now on." % new_user, bold=True))
