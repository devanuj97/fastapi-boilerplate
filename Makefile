run-fmt:
	pipenv run black . --preview

run-vulture:
	pipenv run vulture .

check:
	pipenv run black . --preview
	pipenv run vulture .
	pipenv run isort .
