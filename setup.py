from setuptools import setup

setup(
    name='rpi_checkout',
    version='0.1',
    author="Christopher Jordan-Denny",
    author_email="jordan.denny5@gmail.com",
    url="www.christopherjordan-denny.com",
    packages=['rpi_checkout',],
    license='MIT',
    install_requires=[
        'pygit2>=0.28.1'
    ],
)

