"""
"""
from setuptools import setup, find_packages


setup(name='nagomi',
      version="0.0.1",
      description=(
          'nagomi.'),
      python_requires='>=3.9.0',
      url='https://github.com/nryotaro/nagomi',
      author='Nakamura, Ryotaro',
      author_email='nakamura.ryotaro.kzs@gmail.com',
      license='MIT License',
      classifiers=['Programming Language :: Python :: 3.8'],
      packages=find_packages(),
      install_requires=[
          'click',
          'oauthlib',
          'Flask',
      ],
      entry_points={'console_scripts': ['nagomi=nagomi:main']},
      extras_require={
          'test': [
              'pytest',
          ],
          'dev': [
              'ipython',
              'python-language-server[all]'
          ]})
