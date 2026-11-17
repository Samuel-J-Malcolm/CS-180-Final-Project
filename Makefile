PYTHON = python3
PIP = python3 -m pip
FLASK = python3 -m flask
.PHONY" all install run dev test clean
all: run
install:
	$(PIP) install -r requirements.txt
run:
	$(FLASK) --app app run
dev:
	$(FLASK) --app app run debug
	