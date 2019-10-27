from setuptools import setup

setup(
    name='mtsr',
    version=1.0,
    packages=['mtsr'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['mtsr = mtsr.__main__:main']}
)
