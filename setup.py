from setuptools import find_packages, setup

NAME = "backrooms"
VERSION = "0.0.1"
URL = "https://github.com/SamimiesGames/BackroomsInMinecraft"

AUTHOR = "Samimies"
DESCRIPTION = "Generate backrooms with Python"


setup(
    name=NAME,
    version=VERSION,
    url=URL,
    author=AUTHOR,
    license="MIT",
    description=DESCRIPTION,
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)
