test:
	py.test -f src

lint:
	pep8 src

clean:
	find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +
