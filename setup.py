"""Setup script for extension."""

from setuptools import setup


setup(
    name='grow-ext-html-prettify',
    version='1.0.0',
    license='MIT',
    author='Grow Authors & Nidhi Reddy',
    author_email='nreddy216@gmail.com',
    include_package_data=False,
    packages=[
        'html_prettify',
    ],
    install_requires=[
        'html5lib==0.9999999',
        'lxml==4.6.5'
    ],
)
