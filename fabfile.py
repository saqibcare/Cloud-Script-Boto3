import sys
import time
from fabric.api import env, sudo

# this should be a path to your SSH key for the EC2 instance
key_path = 'Scripts/saqib-key.pem'

def live():
    # DNS entry of our instance
    env.hosts = ['ec2-34-215-230-21.us-west-2.compute.amazonaws.com']
    env.user = 'ubuntu'
    env.key_filename = key_path

def setup_packages():
    sudo('apt-get -y update')
    sudo('apt-get -y dist-upgrade')
    sudo('apt-get install -y python python-django')