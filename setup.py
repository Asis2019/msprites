import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msprites",
    version="1.0.1",
    author="Dharmveer Baloda",
    author_email="dharmvrbaloda836@gmail.com",
    description="Create thumbnail sprite sheet from mp4 media files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asis2019/msprites",
    project_urls={
        "Original": "https://github.com/baloda/msprites",
        "Bug Tracker": "https://github.com/asis2019/msprites/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)