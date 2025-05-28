from setuptools import setup, find_packages

setup(
    name="stockx-sdk",
    version="0.0.1",
    author="Nick",
    license="MIT",
    author_email="njames.programming@gmail.com",
    description="A Python SDK for seamless interaction with the StockX marketplace API",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RoyalGr4pe/stockx-sdk",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    include_package_data=True,
)
