from setuptools import setup, find_packages

setup(
    name='mintty-theme-selector',
    version='1.0',
    description='Command-line theme selector for mintty',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mts=main:main',
        ],
    },
)
