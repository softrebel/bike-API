import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bike-api-softrebel",
    version="0.0.1",
    author="Mohammadreza Shaghouzi",
    author_email="sh.mohammad66@gmail.com",
    description="A small resftull api web framework for request stolen bikes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softrebel/bike-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)