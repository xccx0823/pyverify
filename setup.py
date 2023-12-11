from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version() -> str:
    from pyverify import version
    return version.VERSION


setup(
    name='pyverify',
    version=get_version(),
    author='Ethan',
    author_email='cheerxiong0823@163.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xccx0823/pyverify",
    description='Parameter verification framework based on Python.',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)