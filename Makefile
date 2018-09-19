SHELL := /bin/bash

@PHONY: setup
setup:
	pip3 install discord

run: setup
	source .env && ./main.py
