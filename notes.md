
## Create frontend

open new terminal
In root folder: 
npm create vite@latest
y
project name: frontend
use arrow keys to select react
select javascript + SWC (good for performance)

cd frontend
npm install
npm run dev

Runs on port 5173

## Create backend

create new folder called backend
cd backend

### create virtual environment

/home/emmanora/.local/share/uv/python/cpython-3.13.1-linux-x86_64-gnu/bin/python3.13 -m venv .venv

source .venv/bin/activate

pip install flask
pip install flask-cors

## Readme set up

clone the repo
cd backend
create a file called config.py
Add the following:
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"
