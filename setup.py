import sys
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand

def readme():
    with open('README.md') as f:
        return f.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True

    def run_tests(self):
        if __name__ == '__main__':
            import pytest
            errcode = pytest.main(self.test_args)
            sys.exit(errcode)


if __name__ == '__main__':
    setup(name='vPhon',
      version='0.3.0',
      description='',
      long_description='',
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='phonology vietnamese orthography',
      url='https://github.com/kirbyj/vPhon',
      author='James Kirby',
      author_email='j.kirby@ed.ac.uk',
      packages=['vPhon', 'vPhon.rules'],
    cmdclass={'test': PyTest},
    extras_require={
        'testing': ['pytest'],
    }
      )
