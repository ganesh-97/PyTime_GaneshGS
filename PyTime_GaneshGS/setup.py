import setuptools

with open("D:\PythonTime\README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTime_GaneshGS",
    version="0.0.2",
    author="Ganesh GS",
    author_email="ganeshgs1691997@gmail.com",
    description="package for time conversion from minutes to Hours + minutes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ganesh-97",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
