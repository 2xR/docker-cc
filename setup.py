import pathlib
import re

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent
readme_file = here / "README.rst"
source_file = here / "src" / "docker_cc" / "__init__.py"
version_match = re.search(r"__version__\s*=\s*(['\"])(.*)\1", source_file.read_text())
if version_match is None:
    raise Exception(f"unable to extract version from {source_file}")
version = version_match.group(2)

setup(
    name="docker-cc",
    version=version,
    description="Docker-compose wrapper with added magic ;)",
    long_description=readme_file.read_text(),
    url="https://github.com/2xR/docker-cc",
    author="Rui Jorge Rei",
    author_email="rui.jorge.rei@googlemail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
    ],
    install_requires=["Click", "loguru", "ruamel.yaml"],
    entry_points="""
        [console_scripts]
        docker-cc=docker_cc.cli.main:cli
    """,
    packages=find_packages("src"),
    package_dir={"": "src"},
)
