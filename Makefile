default: test

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

deploy: lock-requirements
	rm Pipfile*
	gcloud app deploy -q app.yaml
	git checkout Pipfile Pipfile.lock

init:
	pipenv install

init-dev:
	pipenv install -d

lock-requirements:
	pipenv lock -r > requirements.txt

run-app:
	FLASK_APP=phd.app FLASK_ENV=development \
	pipenv run flask run

run-test:
	PHD_DB_PASSWORD='pass1' \
	PHD_PASSWORD_SALT='salt1' \
	PHD_SECRET_KEY='secretkey1' \
	pipenv run pytest --flake8 --black --cov=phd --cov-report term-missing tests/

release: clean ## package and upload a release
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload

r: run-app
run: init r
t: run-test
test: init-dev t
