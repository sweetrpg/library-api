import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sweetrpg-library-api",
    version="0.0.1",
    author="Paul Schifferer",
    author_email="paul@schifferers.net",
    description="API microservice for SweetRPG Library data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sweetrpg/library-api",
    project_urls={
        "Bug Tracker": "https://github.com/sweetrpg/library-api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
