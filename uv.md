# install
install via package manager, curl or pip

# init project
uv init my_project

# install packages
uv add requests

# inspect dependency tree
uv tree

# run python file
uv run main.py

# setup dependencies
uv sync 

# remove dependency
uv remove requests

# using pip over uv
uv pip install requests