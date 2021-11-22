import pathlib
from setuptools import setup, find_packages
import os

version = "0.6"

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


dependencies = [
    "pytest"
]

setup(
    name='showcode_forge',
    packages=find_packages(),
    version=version,
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='mit',
    description='Tools for generating code from custom ShowCode Forge questions',
    author='Titusz Ban',
    author_email='tituszban@gmail.com',
    keywords=["showcode"],
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tituszban/showcode_forge",
    install_requires=dependencies,
    setup_requires=dependencies,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            "showcode_forge=showcode_forge.__main__:main"
        ]
    }
)
