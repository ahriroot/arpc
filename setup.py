import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arpc",
    version="0.0.1",
    author="ahriknow",
    author_email="ahriknow@ahriknow.com",
    description="A framework of remote procedure call.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahriroot/arpc-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
