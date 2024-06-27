from setuptools import setup

setup(
    name='gut',
    version='0.1',
    py_modules=['gut'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'gut=gut:cli',
        ],
    },
)