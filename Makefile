.PHONY: clean system-packages python-packages install tests run all

clean:
   find . -type f -name '*.pyc' -delete
   find . -type f -name '*.log' -delete

system-packages:
   sudo apt install python-pip -y

python-packages:
   pip install -r requirements.txt

install: system-packages python-packages

tests:
   python -m unittest discover -s app/test -p '*.py' -v

run:
   $env:FLASK_APP="manage.py"
   flask run

all: clean install tests run

