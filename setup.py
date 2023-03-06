from setuptools import setup

required = [
    "matplotlib",
    "numpy >= 1.20.0",
]

test = [
    "pytest >= 3.7",
]

dev = [
    "pytest-testmon",
    "pytest-watch",
    "check-manifest",
    "twine",
    "tox",
    "black",
    "flake8",
    "mypy",
    "jupyterlab",
]

setup(
    name="bhawick.katas",
    install_requires=required,
    extras_require={
        "dev": dev,
        "test": test,
    },
)
