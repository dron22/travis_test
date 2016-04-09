from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='travis_test',
    version='0.1',
    description='Test travis github integration',
    url='https://github.com/dron22/travis_test',
    author='dron22',
    author_email='info@fastback.io',
    license='MIT',
    packages=['travis_test'],
    install_requires=requirements,
    zip_safe=False
)
