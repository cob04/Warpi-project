# deployment/fabfile.py


import os

from fabric.contrib.files import sed
from fabric.api import env, local, run, task
from fabric.api import env
from fabric.colors import green
from fabric.decorators import hosts


# declare environment global variables

# initialize the base directory
abs_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# rout user
env.user = 'root'

# list of remove IP addresses
env.hosts = ["45.33.51.166"]

# env for the remote server
env.password = 'linode@warpi@serve'

# user name
env.user_name = "cobain"

# ssh key path
env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')


################################
# Configuration and Deployment #
################################

@task
def deploy():
    """
    Configure and deploy to production.
    """
    local( "ansible-playbook ./deploy.yml --private-key=../ssh-keys/45.33.51.166_prod_key\
          -K -u cobain -i ./hosts -vvvv")



################################################
# Server provisioning: Secutiry best practices #
################################################

@task
def provision():
    """
    Prepare a host server for deployment.
    """
    setup_ssh_keys()
    secure()
    upload_keys()
    print(green("Done provisioning"))


@task
def setup_ssh_keys():
    """
    Generate ssh keys and store them in ssh dir.
    """
    # Create directory for a new user
    env.ssh_keys_name = os.path.join(env.ssh_keys_dir, env.host_string + '_prod_key')
    local('ssh-keygen -t rsa -b 2048 -f {0}'.format(env.ssh_keys_name))
    local('cp {0} {1}/authorized_keys'.format(
        env.ssh_keys_name + '.pub',
        env.ssh_keys_dir))
    print(green("generated ssh keys"))


@task
def upload_keys():
    """
    Upload the SSH public/private keys to the server via scp.
    """
    env.ssh_keys_name = os.path.join(env.ssh_keys_dir, env.host_string + '_prod_key')
    scp_command = 'scp {} {}/authorized_keys {}@{}:~/.ssh'.format(
        env.ssh_keys_name + '.pub',
        env.ssh_keys_dir,
        env.user_name,
        env.host_string
    )
    local(scp_command)
    print(green("uploded ssh keys"))


@task
def secure(new_user=env.user_name):
    """
    Minimal security steps for brand new servers.
    Installs system updates, creates new user (with sudo privileges) with "~/.ssh" dir
    for future usage, and disables root login via SSH.
    """
    run("apt-get update -q")
    run("apt-get upgrade -y -q")
    run("adduser --gecos '' %s" % new_user)
    run("usermod -aG sudo %s" % new_user)
    sed('/etc/ssh/sshd_config', '^#PasswordAuthentication yes',
        'PasswordAuthenticaton no')
    run('mkdir /home/{}/.ssh'.format(env.user_name))
    run('chown -R {0} /home/{0}/.ssh'.format(env.user_name))
    run("service ssh restart")
    print(green("Security steps completed. Log in to the server as '%s' from "
                "now on." % new_user, bold=True))
