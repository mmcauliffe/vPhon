
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

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
      packages=['vPhon', 'vPhon.rules']
      )
