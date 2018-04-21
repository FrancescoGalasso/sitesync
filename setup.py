from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='sitesync',
      version='1.0.0',
      description='Script to sync db and/or data from remote host',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Internet',
      ],
      keywords='django test',
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
