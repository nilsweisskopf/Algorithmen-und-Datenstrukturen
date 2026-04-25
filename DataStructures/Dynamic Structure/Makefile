PYTHON = python3
CHECKSTYLE = flake8
PYTHON_FILES = $(shell find . -name "*.py")

all: compile checkstyle test

compile:
	$(PYTHON) -m py_compile $(PYTHON_FILES)

test:
	$(PYTHON) -m doctest $(PYTHON_FILES)

checkstyle:
	$(CHECKSTYLE) $(PYTHON_FILES)

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
