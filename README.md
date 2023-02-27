# Katas.py

[![CI](https://github.com/BhawickJain/katas.py/actions/workflows/ci.yml/badge.svg)](https://github.com/BhawickJain/katas.py/actions/workflows/ci.yml)

My personal repo of Programming, Mathematics, Problem Solving and Computing concept exercises. Here for me to refer back to or comtemplate.

## Get started with Docker

with docker install on your system, run
```
cd docker/
docker compose up
```

enter the container environment with your favourite IDE and run the following in your container terminal,
```
make dev
```
this sets up the virtual environment and dependencies, and installs the library under development in an editable state.

enter the virtual environment,
```
activate
```

check if all packages for development are installed corrected by running the CI tests,
```
make test
```

to exist the virtual environment,
```
deactivate
```