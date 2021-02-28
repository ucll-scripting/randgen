from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('randgen/version.py') as f:
            exec(f.read(), version)

      return version['__version__']



setup(name='randgen',
      version=fetch_version(),
      description='Library to generate random stuff',
      url='http://github.com/ucll-scripting/randgen',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['randgen'],
      entry_points = {
            'console_scripts': [ 'randgen=randgen.shell:main' ]
      },
      include_package_data=True,
      package_data={ '': ['data/*.txt'] },
      install_requires=[
          'lazy',
      ],
      zip_safe=False)
