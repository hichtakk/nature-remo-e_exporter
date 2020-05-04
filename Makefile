.PHONY: install docker

install:
	@poetry install

docker:
	@docker build . -t hichtakk/nature-remo-e-exporter:0.1.0
