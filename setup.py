import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="riskinfo_lk",
    version="0.1",
    author="Vivien Deparday, Ariel Nunez",
    author_email="vivien.deparday@gmail.com",
    description="Code behind riskinfo.lk",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Framework :: GeoNode',
        'License :: OSI Approved :: GNU Library or General Public License (GPL)',
    ],
    license="GPL 3",
    keywords="sri lanka risk geonode django",
    url='https://github.com/vdeparday/riskinfo_lk',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
