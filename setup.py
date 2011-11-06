from setuptools import setup, find_packages
import os

version = '1.0-dev'
tests_require = [
    'plone.app.testing',
    ]

setup(name='plone.app.lockingbehavior',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='dexterity locking behavior plone',
      author='Plone Foundation',
      author_email='mailto:dexterity-development@googlegroups.com',
      url='http://svn.plone.org/svn/plone/plone.app.lockingbehavior/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.behavior',
        'plone.dexterity>1.0b6',
        'plone.locking',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
