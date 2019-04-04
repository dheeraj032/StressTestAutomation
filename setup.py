from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='StressTest',
    version='1.1',
    description='A Generic Stress Test module',
    author='Dheeraj Bajaj',
    author_email='dheeraj.bajaj@wynk.in',
    packages=find_packages(),  # same as name
    # install_requires=[], #external packages as dependencies
)
