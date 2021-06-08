# define the name of the virtual environment directory
VENV := venv
TEST=
PARAMETERS=

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

setup: venv
	./$(VENV)/bin/python3 -m pip install --upgrade pip

run: venv
	./$(VENV)/bin/python3 -m titan

build: venv
	./$(VENV)/bin/python3 setup.py build ${PARAMETERS}

force: venv
	./$(VENV)/bin/python3 setup.py build -f ${PARAMETERS}

install: venv
	./$(VENV)/bin/python3 setup.py install ${PARAMETERS}

test: build
	./$(VENV)/bin/python3 -m pytest ${TEST}

clean:
	rm -rf $(VENV)
	rm -rf build
	rm -rf dist
	rm -rf logs/*
	rm -rf .pytest_cache
	find . -type f -name '*.pyc' -delete

lint:
	 black --target-version=py35 titan setup.py
	 flake8 titan setup.py

doc-build:
	docker-compose build

doc-up:
	docker-compose up -d --build

doc-ls:
	docker-compose ps

doc-logs:
	docker-compose logs -f --tail 15

doc-clean:
	docker-compose down && docker-compose rm

doc-down:
	docker-compose down

