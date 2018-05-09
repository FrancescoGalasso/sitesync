import os
import re
from setuptools import setup

# def readme():
#     with open('README.rst') as f:
#         return f.read()

def get_version(*file_paths):
    """Retrieves the version from django_task/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version("sitesync", "__init__.py")
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(name='sitesync',
      version=version,
      description='Script to sync db and/or data from remote host',
      long_description=readme + '\n\n' + history,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Internet',
      ],
      keywords='django database',
      url='https://github.com/morlandi/sitesync',
      author='Mario Orlandi',
      author_email='morlandi@brainstorm.it',
      license='MIT',
      scripts=['bin/sitesync'],
      packages=['sitesync'],
      # install_requires=[
      #     'markdown',
      # ],
      include_package_data=False,
      zip_safe=False)
