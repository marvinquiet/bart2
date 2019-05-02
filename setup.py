# Time-stamp: <2019-05-01>
'''
Copyright (c) 2019, 2020 Chongzhi Zang, Zhenjia Wang <zhenjia@virginia.edu>, Wenjing Ma <wm9tr@virginia.edu>

This code is free software; you can redistribute it and/or modify it 
under the terms of the BSD License.

@status: release candidate
@version: $Id$
@author: Chongzhi Zang, Zhenjia Wang, Wenjing Ma
@contact: zhenjia@virginia.edu, wm9tr@virginia.edu
'''


import os,sys
from setuptools import setup, find_packages
from codecs import open
from os import path
import BART

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


def main():
    if float(sys.version[:3])<3.0:
        sys.stderr.write("CRITICAL: Python version must be higher than or equal to 3.0!\n")
        sys.exit(1)
        
    setup(name="BART",
          version=BART.__version__,
          description="Binding Analysis for Regulatory Transcription Factors of Genes - Revised version",
          long_description=long_descr,
          author='Zhanjia Wang, Wenjing Ma',
          author_email='zhenjia@virginia.edu, wm9tr@virginia.edu',
          url='https://github.com/marvinquiet/revised_BART',
          # packages=find_packages(),#['BART'],
          packages=['BART'],
          package_data={'':['bart.conf'],
                        'BART':['hg38_library/*.dat',
                                'hg38_library/*.bed',
                                'hg38_library/*.json',
                                'hg38_library/*.h5',
                                'hg38_library/hg38_test_data/*',
                                'mm10_library/*.dat',
                                'mm10_library/*.bed',
                                'mm10_library/*.json',
                                'mm10_library/*.h5',
                                'mm10_library/mm10_test_data/*'],},
          #data_files=[('.',['bart.conf'])],
          #include_package_data=True,
          # scripts=['bin/bart',],
          entry_points = {
              "console_scripts": ['revised_bart = BART.bart:main']
              },
          classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: Science/Research',
              'License ::',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: POSIX',
              'Topic :: Scientific/Engineering :: Bio-Informatics',
              'Programming Language :: Python',
              ],
          install_requires=[
              'argparse',
              'configparser',
              'pyyaml',
              'numpy',
              'pandas',
              'scipy',
              ],
          #cmdclass = command_classes,
          
          )

if __name__=='__main__': 
    main()         
