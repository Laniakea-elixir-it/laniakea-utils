'''
laniakea-utils
Utilities for Laniakea applications
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name='laniakea-utils',
  version="0.1.1",
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
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: POSIX :: Linux",
  ],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.6",
  install_requires=[
          'Flask==2.0.2',
          'flaat==0.14.7',
          'gunicorn==20.1.0',
          'hvac==0.11.2'
      ],
  data_files=[('etc/laniakea',['config/laniakea-utils.ini'])],
)
