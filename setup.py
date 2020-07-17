import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="resourcer", # Replace with your own username
    version="0.1.4",
    author="Fiaz Sami",
    description="An object wrapper around 'requests'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fiazsami/resourcer",
    packages=['resourcer',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires='>=3.6',
)