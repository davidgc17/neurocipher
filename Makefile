# Variables
PYTHON=python
SRC=src
MAIN=$(SRC)/main.py
TEST_DIR=tests

# Ejecutar el programa principal
run:
	$(PYTHON) $(MAIN)

# Ejecutar tests con unittest
test:
	set PYTHONPATH=$(SRC) && $(PYTHON) -m unittest discover $(TEST_DIR)

# Placeholder para limpieza (logs, en el futuro)
clean:
	@echo "Limpieza no implementada aún. Se añadirá con el sistema de logs."
