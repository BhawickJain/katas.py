SHELL := /bin/bash
.PHONY = compile help
.DEFAULT_GOAL = help

venv: check-os
    # Create venv if it doesn't exist
    # test -d venv || virtualenv -p python3 --no-site-packages venv
	#test -d venv || python3 -m venv ~/.local/.venv
	@echo -e $$'\n\e[1;42m\e[1;30m INITIALISING VENV \e[0m\n'
	python3 -m venv $(VENVPATH)

dev: check-os venv
	@echo -e $$'\n\e[1;44m\e[1;37m DEVELOPMENT \e[1;42m\e[1;30m ACTIVATING VENV AND INSTALLING PACKAGES \e[0m\n'
	( \
       source $(VENVPATH)/bin/activate; \
       pip install -e .[dev]\
    )
	@echo -e $$'\n\e[1;42m\e[1;30m DONE! \e[0m\n'
	@echo -e $$'\e[1;34mto activate environment, type:\e[0m'
	@echo -e $$'activate'
	@echo -e $$''
	@echo -e $$'\e[1;34mto deactivate environment, type:\e[0m'
	@echo -e $$'deactvate'
	@echo -e $$''

build-check: check-os
	python setup.py sdist

build: check-os depreciated
	python setup.py bdist_wheel sdist

publish: check-os
	make build-check
	twine upload dist/*

test: check-os
	bash scripts/run_tests.sh

# only test changes on default python installation
test-watch: check-os
	@ptw --spool 200 -c --beforerun "echo $$'\n\e[1;42m\e[1;30m PYTEST WATCH \e[0m\n'" --runner "pytest --testmon" --afterrun "echo '\ncontrol + c to stop'"

patch: check-os
	git push && bumpversion patch setup.cfg && git push --tags

clean:
	@bash scripts/clean-ignored-files.sh

depreciated:
			echo -e $$'\e[1;103m\e[1;90m DEPRECIATED \e[0m\e[1;97m This make recipe to be removed \e[0m\n' ;\

check-os:
	@(\
		if [[ $(shell uname) == "Darwin" ]]; then \
			echo -e $$'\e[1;103m\e[1;90m WARNING \e[0m\e[1;97m Script only tested on Debian OS (macOS detected) \e[0m' ;\
		fi \
	)

help: check-os
	@echo -e $$'\n\e[1;44m\e[1;37m HELP \e[0m\n'
	@echo -e $$'\e[1;34minstall dev environment:\e[0m	make dev'
	@echo -e $$'\e[1;34mactivate environment:\e[0m 		activate'
	@echo -e $$'\e[1;34mdeactivate environment:\e[0m 	deactivate'
	@echo -e $$'\e[1;34mtype check:\e[0m			mypy <directory or file>'
	@echo -e $$'\e[1;34mformat:\e[0m				black <directory or file>'
	@echo -e $$'\e[1;34mtest file:\e[0m			pytest <file>'
	@echo -e $$'\e[1;34mrun prettier in neovim:\e[0m		:CocCommand prettier.formatFile'
	@echo -e $$''
