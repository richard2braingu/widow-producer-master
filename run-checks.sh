#!/bin/bash

PRECOMMIT=.git/hooks/pre-commit
if [ -f "$PRECOMMIT" ];
then
  echo "Removing pre-commit TYPE pre-commit..."
  rm $PRECOMMIT
fi

PREPUSH=.git/hooks/pre-push
if ! [ -f "$PREPUSH" ];
then
  echo "Installing pre-commit TYPE pre-push..."
  pre-commit install -t pre-push
fi

# Run tests, linters, and formatters
if [[ $1 == "coverage" ]]
then
    coverage run -m pytest
    coverage html
    coverage report
elif [[ $1 == "flake" ]]
then
    echo "Running flake8... "
    flake8 .
elif [[ $1 == "isort" ]]
then
    echo "Running isort... "
    isort .
elif [[ $1 == "black" ]]
then
    echo "Running black... "
    black .
elif [[ $1 == "pylint" ]]
then
    echo "Running pylint... "
    ./pylint.sh
else
    echo "Running flake8... "
    flake8 .
    echo "Running isort... "
    isort .
    echo "Running black... "
    black .
    echo "Running pylint... "
    ./pylint.sh
    echo "Running Coverage Report"
    coverage run -m pytest
    coverage html -i
    coverage report -i
fi