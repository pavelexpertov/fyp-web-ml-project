# fyp-web-ml-project
My final year project (2017/18) for Software Engineering Beng

# How to make it run

## Vagrant (recommended)
All you do is to go to a root directory and then execute `vagrant up` if you have not set up at all. Then just go to [localhost:8080](http://localhost:8080)

If you already set it up and then you start it from off, it's recommended to run `vagrant reload --provision` so that mongodb service can be restarted.

Keep in mind these operations may take a long time to execute.

*Note*: Windows users need to change line endings from crlf to lf endings for all shell script files in set_up_scripts/vagrant_provisioning_scripts folder. For Unix and Linux, it should be fine as it is.

Here's a [link](https://www.vagrantup.com/downloads.html) to install Vagrant and another [link](https://www.virtualbox.org/) to install virtualbox that need it as its dependency.

## Manual set up via venv

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir db_data

# Execute below command in a separate terminal or tab but in the same root directory
mongod --dbpath=db_data

python set_up_scripts/create_db.py
cd vue-ui
npm install
npm run build
cd ..
pip install --editable .
export FLASK_APP=fyp_web_ml_project
flask run
# An address should be displayed at the bottom of the terminal
```

## Requirements
- Node version 8.11.1
- npm 5.6.0
- virtualbox 5.1.34
- Vagrant 2.0.2
- db version v3.6.3
