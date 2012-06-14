from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='fibo',
      version=version,
      description="ejemplo fibonacci",
      long_description="""\
ejemplo fibonacciiiiii""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='paquete fibo',
      author='Elvis Garcia',
      author_email='elvisjonasg@gmail.com',
      url='https://github.com/ejgarciavtv/fibo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
