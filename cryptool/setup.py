from setuptools import setup, find_packages

setup(
    name="cryptool",
    version="1.0.0",
    author="Phath Sopheakmeangkuol",
    author_email="phathsopheakmeangkuol2007@email.com",
    description="A command-line cryptography toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/phathsopheakmeangkuol2007-netizen/cryptool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.6",
    install_requires=[
        "cryptography>=3.0",
    ],
    entry_points={
        "console_scripts": [
            "cryptool=cryptool.cli:main",
        ],
    },
)
