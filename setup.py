import json
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().split("\n")

with open("package_info.json", "r", encoding="utf-8") as f:
    package_info = json.load(f)

setuptools.setup(
    name="MyFaceAI",
    version=package_info["version"],
    author="Tejaswi Tadelu",
    author_email="tadelutejaswi709@gmail.com",
    description=(
        "A Lightweight Face Recognition and Facial Attribute Analysis Framework"
        " (Age, Gender, Emotion, Race) for Python"
    ),
    data_files=[("", ["README.md", "requirements.txt", "package_info.json"])],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tejaswitadelu/MyFaceAI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["MyFaceAI =MyFaceAI.MyFaceAI:cli"],
    },
    python_requires=">=3.7",
    install_requires=requirements,
)
