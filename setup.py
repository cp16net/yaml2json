from setuptools import setup
from setuptools import find_packages

setup(
    name='yaml2json',
    version='0.1',
    description='Convert yaml to json',
    author='Craig Vyvial',
    author_email='cp16net@gmail.com',
    license='Apache',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={
        'console_scripts': [
            'yaml2json=yaml2json.yaml2json:main',
        ]
    }
)
