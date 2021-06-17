from setuptools import setup, find_packages
import os

version = "0.1"


dependencies = [
    
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
    keywords=[],
    install_requires=dependencies,
    setup_requires=dependencies,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            "showcode_forge=showcode_forge.__main__:main"
        ]
    }
)
