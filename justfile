# just --working-directory . --justfile test/justfile

default: lint typecheck

lint:
  pylint vim

typecheck:
  mypy vim
