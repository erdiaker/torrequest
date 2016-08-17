from setuptools import setup

setup(name='torrequest',
  version='0.1.0',
  description='A simple interface for HTTP(s) requests over Tor',
  url='http://github.com/erdiaker/torrequest',
  author='Erdi Aker',
  author_email='erdiaker@gmail.com',
  license='MIT',
  py_modules=['torrequest'],
  install_requires=[
    'PySocks>=1.5.7',
    'requests>=2.11.0',
    'stem>=1.4.0'
  ],
  zip_safe=False)

