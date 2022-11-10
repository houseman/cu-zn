# === COLORS ===
RED     := $(shell tput -Txterm setaf 1)
GREEN   := $(shell tput -Txterm setaf 2)
YELLOW  := $(shell tput -Txterm setaf 3)
BLUE    := $(shell tput -Txterm setaf 4)
PURPLE  := $(shell tput -Txterm setaf 5)
CYAN    := $(shell tput -Txterm setaf 6)
WHITE   := $(shell tput -Txterm setaf 7)
BOLD   	:= $(shell tput -Txterm bold)
RESET   := $(shell tput -Txterm sgr0)

TEST_OPTS ?=
PIP_COMPILE_ARGS = --upgrade --no-emit-index-url --no-emit-trusted-host

pip-compile:
	@python -m piptools compile --version &> /dev/null || (echo "Installing pip-tools" && python -m pip install --quiet pip-tools)
	CUSTOM_COMPILE_COMMAND="make update-deps" python -m piptools compile  $(PIP_COMPILE_ARGS) --output-file requirements/requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make update-deps" python -m piptools compile  $(PIP_COMPILE_ARGS) --extra dev --output-file requirements/dev-requirements.txt pyproject.toml

## Install dependencies and ensure they are synced
pip-sync:
	@python -m piptools sync --version &> /dev/null || (echo "Installing pip-tools" && python -m pip install --quiet pip-tools)
	python -m piptools sync requirements/requirements.txt requirements/dev-requirements.txt
	python -m pip install --no-deps --disable-pip-version-check --quiet --editable .

update-deps: pip-compile pip-sync
install-deps: pip-sync

.PHONY: pip-compile pip-sync update-deps install-deps

.PHONY: test
test:
	@echo "\n${BLUE}Run unit tests${RESET}"
	python -m pytest $(TEST_OPTS)
	@echo "\n${BLUE}Done unit tests${RESET}"

PHONY: run-nox
run-nox:
	@nox --version &> /dev/null || (echo "Reuires nox" && exit 1)
	@echo "\n${BLUE}Run nox${RESET}"
	nox --reuse-existing-virtualenvs
	@echo "\n${BLUE}Done nox${RESET}"

.PHONY: lint
lint:
	@echo "\n${BLUE}Run linting${RESET}"
	@echo "\n${CYAN}Running pyupgrade${RESET}"
	pyupgrade
	@echo "\n${CYAN}Running isort${RESET}"
	isort src tests
	@echo "\n${CYAN}Running black${RESET}"
	black src tests
	@echo "\n${CYAN}Running flake8${RESET}"
	flake8
	@echo "\n${CYAN}Running mypy${RESET}"
	mypy src
	@echo "\n${BLUE}Done linting${RESET}"
