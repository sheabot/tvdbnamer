import os
from setuptools import find_packages, setup


# Dynamically calculate the version based on tvdbnamer.VERSION.
version = __import__('tvdbnamer').__version__


setup(
    name='tvdbnamer',
    version=version,
    url='https://github.com/sheabot/tvdbnamer/',
    author='sheabot',
    description=('A TV show file renamer based on data from TheTVDB'),
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
