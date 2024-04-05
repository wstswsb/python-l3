lint:
	mypy --strict .
	ruff check . --fix
	ruff format .

profile:
	LINE_PROFILE=1 python sha_prof.py
	python -m line_profiler -rtmz profile_output.lprof
	rm profile_output*
	
