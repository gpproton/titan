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

dk_build:
	docker-compose build

dk_up:
	docker-compose up -d --build

dk_ls:
	docker-compose ps

dk_logs:
	docker-compose logs -f --tail 15

dk_clean:
	docker-compose down && docker-compose rm

dk_down:
	docker-compose down

lint:
	 flake8 titan setup.py
	 black --target-version=py35 titan setup.py

