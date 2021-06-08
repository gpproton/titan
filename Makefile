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

build:
	./$(VENV)/bin/python3 setup.py build ${PARAMETERS}

force:
	./$(VENV)/bin/python3 setup.py build -f ${PARAMETERS}

install:
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

docker_build:
	docker-compose build

docker_up:
	docker-compose up -d --build

docker_clean:
	docker-compose down && docker-compose rm

docker_down:
	docker-compose down

# lint:
#    ./bin/flake8.sh

lint-fix:
	 black --target-version=py35 .

