import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests>=2.21.0", "russtress"]

setuptools.setup(
    name="csl_accent",
    version="0.0.1",
    author="Julia Korotkova, Panteleimon Korolev",
    author_email="pantlmn@gmail.com",
    description="A package for putting stress marks in Church Slavonic texts in grazhdanitsa encoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pantlmn/csl_accent",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)
