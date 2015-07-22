import os
from os.path import join, dirname, split
# from distutils.core import setup
from setuptools import setup


def path_tokens(path):
    if not path:
        return []
    head, tail = split(path)
    return path_tokens(head) + [tail]


def get_packages():
    exclude_pacakages = ('__pycache__',)
    packages = []
    for path_info in os.walk('src'):
        tokens = path_tokens(path_info[0])
        if tokens[-1] not in exclude_pacakages:
            packages.append('.'.join(tokens))
    return packages


with open('requirements.txt', 'r') as f:
    requirements = f.readlines()


setup(name='edx_sso_npoed',
      version='2.0',
      install_requires=requirements,
      packages=['pipeline', 'backends'],
      zip_safe=False,
      # packages=get_packages(),
      )
