#!/usr/bin/env bash
echo "---INSTALLING Pipfile TO VIRTUALENV---"
pipenv --rm && pipenv --python 3.7
pipenv run pip install Cython
pipenv lock --keep-outdated -r --dev | pipenv run pip install -U -r /dev/stdin

echo "---CREATING LOCAL REQUIREMENTS FILE---"
pipenv lock --keep-outdated -r > ./requirements.txt
