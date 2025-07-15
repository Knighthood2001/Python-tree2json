from setuptools import setup, find_packages

setup(
    name="tree2json",
    version="0.1.4",
    description="将项目目录树字符串转换为JSON结构",
    author="knighthood2001",
    url="https://github.com/Knighthood2001/Python-tree2json", 
    packages=find_packages(),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
