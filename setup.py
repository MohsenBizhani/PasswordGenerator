from setuptools import setup, find_packages

setup(
    name="passkey-generator-cli",
    version="1.0.0",
    author="Mohsen Bizhani",
    author_email="bizhani.2002@gmail.com",
    description="A secure and customizable password generator CLI tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MohsenBizhani/PasswordGenerator",
    packages=find_packages(),
    install_requires=[
        "pyperclip>=1.8.2"
    ],
    entry_points={
        "console_scripts": [
            "password-generator=password_generator:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)