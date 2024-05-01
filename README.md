# fyp-web-ml-project
My final year project (2017/18) for Software Engineering Beng

The purpose of the project is to implement a final year project along with
a dissertation. The project is about allowing users to play around with machine
learning algorithms via a web user interface and see results of their trainings
and accuracy tests against provided data structures.

There are two components that compose the project:
- Python backend: it is a [Flask](https://flask.palletsprojects.com/en/3.0.x/)
application that contains logic for training and interacting with models via API
endpoints. It uses scikit-learn dependency to expose machine learning algorithms
to the users.
  - These can be found in `fyp_web_ml_project` directory. Examples of how
some of its operations work can be found in `tests` directory.
- NodeJs frontend: it is a [VueJS](https://v2.vuejs.org/) application with a
  user interface that allow users to interact with the algorithms and train
  them. The implementation of this can be found in `vue-ui` directory.

# How to make it run

**WARNING**: Unfortunately, it is not possible to run the project due to very
old dependencies at both Python and NodeJs levels. Attempts have been made to
get them to work, but their 'dysfunctional' nature prevents the project from
being started up.

## Vagrant (recommended)
All you do is to go to a root directory and then execute `vagrant up` if you
have not set up at all. Then just go to [localhost:8080](http://localhost:8080)

If you already set it up and then you start it from off, it's recommended to run
`vagrant reload --provision` so that mongodb service can be restarted.

Keep in mind these operations may take a long time to execute.

*Note*: Windows users need to change line endings from crlf to lf endings for
all shell script files in set_up_scripts/vagrant_provisioning_scripts folder.
For Unix and Linux, it should be fine as it is.

Here's a [link](https://www.vagrantup.com/downloads.html) to install Vagrant and
another [link](https://www.virtualbox.org/) to install virtualbox that need it
as its dependency.

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
- Python 3.6.2
