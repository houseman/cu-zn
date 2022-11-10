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

.PHONY: pip-compile
## Compiles and updates dependencies (runs 'deps' afterwards)
pip-compile: pip-sync
	@pip-compile --version &> /dev/null || (echo "Installing pip-tools" && pip install --quiet pip-tools)
	CUSTOM_COMPILE_COMMAND="make pip-compile" pip-compile $(PIP_COMPILE_ARGS) --output-file requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make pip-compile" pip-compile $(PIP_COMPILE_ARGS) --extra dev --output-file dev-requirements.txt pyproject.toml

.PHONY: pip-sync
## Install dependencies and ensure they are synced
pip-sync:
	@pip-sync --version &> /dev/null || (echo "Installing pip-tools" && pip install --quiet pip-tools)
	pip-sync requirements.txt dev-requirements.txt
	pip install --no-deps --disable-pip-version-check --quiet --editable .

.PHONY: test
test:
	@echo "\n${BLUE}Run unit tests${RESET}"
	pytest $(TEST_OPTS)
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
