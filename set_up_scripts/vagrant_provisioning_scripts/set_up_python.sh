#!/usr/bin/env bash

# Setting up python dependencies
sudo apt-get install -y python3-pip python3-setuptools
wget https://files.pythonhosted.org/packages/c4/44/e6b8056b6c8f2bfd1445cc9990f478930d8e3459e9dbf5b8e2d2922d64d3/pip-9.0.3.tar.gz
tar -xzvf pip-9.0.3.tar.gz
cd pip-9.0.3
python3 setup.py install
#pip3 install -U pip
sudo pip3 install virtualenv
