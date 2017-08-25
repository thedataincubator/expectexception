#!/usr/bin/env python

from setuptools import setup

setup(
    name='ExpectException',
    version='0.1.1',
    description='Jupyter magic for exceptions',
    long_description='Display exceptions and tracebacks in Jupyter notebooks without halting execution.',
    author='Robert Schroll',
    author_email='robert@thedataincubator.com',
    url='https://github.com/thedataincubator/expectexception',
    packages=['expectexception'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
