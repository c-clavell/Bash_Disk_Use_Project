install:
	python -m pip install --upgrade pip &&\
	python -m pip install -r requirements.txt

test:
	python -m pytest -vv tests

format:
	black *.py

lint:
	pylint --disable=R,C disk_report.py

all: install lint test