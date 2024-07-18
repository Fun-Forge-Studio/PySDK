from setuptools import find_packages, setup

with open('README.md', 'r') as file:
    setup(
        name='pysdk',
        version='0.1.0',
        description='',
        long_description=f'{file.read()}\n',
        author='Fun Forge Studio',
        maintainer='DevByEagle',
        packages=find_packages(include=['pysdk'], exclude=['test']),
        url='https://github.com/Fun-Forge-Studio/PySDK',
        download_url='https://github.com/Fun-Forge-Studio/PySDK/releases',
        platforms=['Windows', 'Linux']
    )