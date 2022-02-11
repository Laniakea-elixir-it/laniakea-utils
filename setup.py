'''
laniakea-utils
Utilities for Laniakea applications
'''

from setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name='laniakea-utils',
  version="0.0.1",
  author="Marco Antonio Tangaro",
  description='Utilities for Laniakea applications',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/Laniakea-elixir-it/laniakea-utils',
  project_urls={
    "Bug Tracker": "https://github.com/Laniakea-elixir-it/laniakea-utils/issues",
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License, version 3",
    "Operating System :: Linux",
  ],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.6",
)
