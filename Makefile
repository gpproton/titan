# define the name of the virtual environment directory
VENV := env
TEST=
PARAMETERS=

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate:

setup: python3 -m venv $(VENV)
	$(VENV)/bin/activate
	python3 -m pip install --upgrade wheel pip pipenv psycopg2-binary black flake8 Django
	python3 -m pipenv install --skip-lock

# venv is a shortcut target
venv: $(VENV)/bin/activate

update:
	python3 -m pipenv update

dev: venv
	python3 manage.py runserver

run: dev
# python3 -m pipenv run python -m titan ${PARAMETERS}

# build: venv
# 	python3 -m pipenv run python run setup.py build ${PARAMETERS}

# force: venv
# 	python3 -m pipenv run python setup.py build -f ${PARAMETERS}

# test: build
# 	python3 -m pipenv run python -m pytest ${TEST}

clean:
	pipenv --rm;rm -rf {$(VENV),env,build,dist,titan.egg-info,logs/*};rm -rf .pytest_cache;find . -type f -name '*.pyc' -delete

lint:
	 python3 -m pipenv run python -m black --target-version=py35 titan setup.py
	 python3 -m pipenv run python -m flake8 titan setup.py

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

