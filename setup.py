from os import path
from setuptools import setup, find_packages

with open(path.join(".", 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="automate-home",
      version="0.9.1",
      description="A python3 library to automate (home) devices",
      url="https://github.com/majamassarini/automate-home",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="Maja Massarini",
      author_email="maja.massarini@gmail.com",
      license="GPLv3",
      classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3.8",
            "Topic :: Communications",
            "Intended Audience :: Developers",
      ],
      packages=find_packages(exclude=[]),
      include_package_data=True,
      install_requires=['APScheduler==3.9.0', 'hiredis==1.1.0', 'aioredis==1.3.1', 'ephem', 'pytz', 'PyYAML']
      )
