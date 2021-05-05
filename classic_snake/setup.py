import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sky-classic_snake", # Replace with your own username
    version="0.0.1",
    author="Kuang-Ying ivyshih",
    author_email="ivyshih@yahoo.com",
    description="Classic Snake Game by SKY",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivyshihwork/python/game/classic_snake",
    project_urls={
        "Bug Tracker": "https://github.com/ivyshihwork/python/game/classic_snake/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
