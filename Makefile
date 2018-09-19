SHELL := /bin/bash

@PHONY: setup
setup:
	pip3 install discord.py==0.16.12

run: setup
	source .env && ./main.py
