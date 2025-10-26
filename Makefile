install:
	uv sync

lint:
	uv run ruff check .

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

runserver:
	uv run python3 manage.py runserver

shell:
	uv run manage.py shell_plus --ipython