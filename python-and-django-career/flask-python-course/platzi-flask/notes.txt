# Install python3
# Install pip

# Install virtualenv
virtualenv venv 
venv\Scripts\activate

# option 1
pip install flask
# option 2
pip install -r requirements.txt

# SET VARIABLE TO RUN FLASK
# mac and linux
export FLASK_APP=main.py

# windows
# set FLASK_APP=main.py
$env:FLASK_APP = "main.py"

# run flask
flask run

# Debugging en Flask
$env:FLASK_DEBUG = 0 #do not show errors
$env:FLASK_DEBUG = 1 #show errors

# change environment to development
$env:FLASK_ENV='production'
$env:FLASK_ENV='development' 

# Install wtf
pip install -r requirements.txt