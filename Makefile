lint:
	mypy --strict .
	ruff check --fix .
