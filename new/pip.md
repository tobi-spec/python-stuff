# install
ships with python

# init project - 1
python3 -m venv .venv

# init project - 2
source .venv/bin/activate.bat

# install packages
pip3 install requests

# inspect dependencies
pip list

# create requirements.txt
pip3 freeze > requirements.txt

# run python file
python3 main.py

# remove dependency
pip3 uninstall requests


