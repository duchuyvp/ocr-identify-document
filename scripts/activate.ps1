python -m venv ./env

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

env/Scripts/activate

python -m pip install --upgrade pip

pip install -r requirements.txt