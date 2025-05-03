# lib_version

A version-aware library that provides functionality to output its own version number.

### Description

This package implements a simple mechanism to retrieve and display the version of the library itself. This is useful for verification purposes and dependency management.

### Installation

You can install the package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/remla25-team8/lib-version.git@v<selected-version>
```

Replace `<selected-version>`\_` with your desired version number (e.g., 0.1.9). Make sure that the verson is covered.

### Usage

After installation, you can verify the package is working correctly with the following command from terminal:

```bash
python -c "from lib_version import print_version; print_version()"
```

This will print the installed version number to the console. The output should match the `<selected-version>` you specified during installation.

### Environment Setup (testing)

It's recommended to test the package in an isolated environment. You can create one using either venv or conda.

#### Using conda

```bash
# Create a new conda environment
conda create -n lib-version-test

# Activate the environment
conda activate lib-version-test

# Install the package and test it
pip install git+https://github.com/remla25-team8/lib-version.git@v<selected-version>
python -c "from lib_version import print_version; print_version()"
```

#### Using venv

```bash
# Create a new virtual environment
python -m venv lib-version-test

# Activate the environment (Linux/Mac)
source lib-version-test/bin/activate

# Install the package and test it
pip install git+https://github.com/remla25-team8/lib-version.git@v<selected-version>
python -c "from lib_version import print_version; print_version()"
```
