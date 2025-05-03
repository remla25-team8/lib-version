from setuptools import setup, find_packages

setup(
    name="lib_version",
    description="A simple package to print its version number",
    author="team8",
    author_email="Y.Huang-51@student.tudelft.nl",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    extras_require={"dev": ["pytest"]}
)