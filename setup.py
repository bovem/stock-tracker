import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock-tracker",
    version="1.0.0",
    author="Avnish",
    author_email="av_nish@outlook.com",
    description="Stock Tracker is an interactive data visualization application developed in Python, with the help of Dash, iexfinance and Pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avnish98/stock-tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
