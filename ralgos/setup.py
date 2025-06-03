from skbuild import setup
from setuptools import find_packages

setup(
    name="ralgos",
    version="0.1",
    description="Randomized Algorithms Library with k-wise sampling",
    author="Nimitt",
    packages=find_packages(),
    include_package_data=True, 
    package_data={
        "ralgos": ["*.so"],  
    },
    python_requires=">=3.8",
    cmake_install_target="",
)
