VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
  VIRTUALENV = /usr/local/python/bin/virtualenv
endif


install: venv
	. venv/bin/activate; pip install -r requirements.txt \
		--download-cache /tmp/pipcache

venv:
	$(VIRTUALENV) venv

run: venv
	. venv/bin/activate; python app/app.py
	
clean:
	rm -rf venv
