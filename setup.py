from setuptools import setup, find_packages

setup(
        name = 'SnakeOil',
        version = '0.1',
        packages = find_packages(),
        scripts = ['snakeoil.py' ],
        install_requires = ['requests>=2.4.1'],
        author = 'Jeff Smith',
        author_email = 'jeff@allthingsdork.com',
        description = ' A Python API for the Transmission Daemon',
        license = 'PSF',
        keywords = 'transmission api torrent',
        url = 'http://github.com/bobbidigital/snakeoil'
)

