#!/usr/bin/env python

import setuptools

setuptools.setup(name='gributils-annotator',
      version='0.11',
      description='Weather annotation service for streams of newline sepratade json positional messages based on gributils',
      long_description="""Weather annotation service for streams of newline sepratade json positional messages based on gributils""",
      long_description_content_type="text/markdown",
      author='Egil Moeller',
      author_email='egil@innovationgarage.no',
      url='https://github.com/innovationgarage/gributils-annotator',
      packages=setuptools.find_packages(),
      install_requires=[
          'socket-tentacles>=0.0.9',
          'click',
          'requests'
      ],
      include_package_data=True,
      entry_points='''
      [console_scripts]
      gributils-annotator = gributils_annotator.cli:main
      '''
  )
