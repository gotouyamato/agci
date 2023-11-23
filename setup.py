import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agci",
    version="0.0.1",
    author="yamato goto",
    author_email="s2122100@stu.musashino-u.ac.jp",
    description="A package for agci",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/gotouyamato",
    project_urls={
        "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['bugcount'],
   # packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'bugcount = bugcount:main'
        ]
    },
)
