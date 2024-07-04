JYTHON := $(shell which jython)
JYTHON_CACHE_DIR := $$HOME/.cache/jython

.DEFAULT_GOAL := help

##@ Help

.PHONY: help clean check init install install-clean install-force install-nocache install-nodeps

help: ## Display this help message.
	@awk \
		'BEGIN { \
			FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n" \
		} \
		/^[a-zA-Z_-]+:.*?##/ { \
			printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2 \
		} \
		/^##@/ { \
			printf "\n\033[1m%s\033[0m\n", substr($$0, 5) \
		} ' \
		$(MAKEFILE_LIST)

##@ Cleanup

clean: check ## Uninstall all Jython packages.
	@ echo "Uninstalling all Jython packages…"
	jython -m pip freeze | xargs jython -m pip uninstall -y

##@ Initialize

check: ## Check if Jython is installed.
	@if test ! -x "$(JYTHON)"; then \
		echo "ERROR: Jython was not found. Please install it first, or add it to PATH."; \
		false; \
	fi
	@$(JYTHON) --version

init: ## Run check and create required directories for other targets.
	@echo "Initializing…"
	@mkdir -p "$(JYTHON_CACHE_DIR)"

##@ Install
install: check init ## Install this package using Jython with caching enabled.
	@echo "Installing package…"
	jython -m pip install --cache-dir="$(JYTHON_CACHE_DIR)" .

install-clean: check init clean ## Perform clean installation using Jython with caching enabled.
	@echo "Running clean install…"
	jython -m pip install --cache-dir="$(JYTHON_CACHE_DIR)" .

install-force: check init ## Reinstall all packages using Jython even if they are already up-to-date.
	@echo "Reinstalling all packages…"
	jython -m pip install --force-reinstall --cache-dir="$(JYTHON_CACHE_DIR)" .

install-nocache: check ## Install this package using Jython with caching disabled.
	@echo "Installing packages (no cache)…"
	jython -m pip install --no-cache-dir .

install-nodeps: check ## Install this package without dependencies.
	@echo "Installing package without dependencies…"
	jython -m pip install --no-deps .