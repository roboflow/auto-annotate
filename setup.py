import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="a2",
    version='1.0.0',
    python_requires=">=3.7",
    description="Simple dataset auto annotation tool leveraging Roboflow API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/roboflow-ai/auto-annotate",
    author="Piotr Skalski",
    author_email="piotr.skalski92@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "roboflow",
        "tqdm"
    ],
    extras_require={},
    classifiers=[]
)