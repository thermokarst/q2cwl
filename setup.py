from setuptools import setup, find_packages

setup(
    name='q2cwl',
    version='0.0.1',
    license='BSD-3-Clause',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['q2cwl=q2cwl:root']})
