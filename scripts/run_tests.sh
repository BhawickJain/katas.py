#!/bin/zsh

# Script to run all tests, like a local CI pipeline

set -e

echo -e "\n\e[1;42m\e[1;30m CODE STYLES \e[0m\n"
black katas/ tests/

echo -e "\n\e[1;42m\e[1;30m CODE LINT \e[0m\n"
# flake8 katas/ tests/
echo "Code lint disabled"

echo -e "\n\e[1;42m\e[1;30m TYPE CHECK \e[0m\n"
mypy --implicit-reexport --namespace-packages katas

echo -e "\n\e[1;42m\e[1;30m UNIT TESTS \e[0m\n"
tox
