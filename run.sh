# Only run this script when you have the conda environment installed called 'cleaning-data'.
# In order to do that, you need to set it up using the conda_environment.yml with the appropriate conda command.
source activate cleaning-data
pip install --editable .
export FLASK_APP=fyp-web-ml-project
export FLASK_DEBUG=true
flask run
