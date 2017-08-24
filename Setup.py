from setuptools import setup

setup(
    name='Calculator',
    version='2.1',
    packages=['Calculator.py'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)