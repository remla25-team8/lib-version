# lib-version

Utility library that exposes its own version for downstream services.

## Features

- **Version-aware library**: Query its own version through the `VersionUtil` class
- **Metadata-based version retrieval**: Version information is extracted from packaging metadata or injected by CI/CD
- **External dependency support**: Can be reused as an external dependency by other components like `app`
- **Automated CI/CD workflows**: Automatic packaging and publishing to supported package registries
- **Multiple pre-release iterations**: Support for creating multiple iterations of the same pre-release version

## Usage

```python
from lib_version import VersionUtil

# Print the version
VersionUtil.print_version()

# Get the version as a string
version = VersionUtil.get_version()
print(f"Current version: {version}")
```

## CI/CD Workflows

### 1. Standard Release (`publish.yaml`)
- Triggers on Git tags (e.g., `v1.2.3`)
- Automatically injects version into package
- Publishes to GitHub Releases

### 2. Pre-release Creation (`preRelease.yml`)
- Triggers when a stable release is published
- Automatically creates the next pre-release version (e.g., `v1.2.4-pre-1`)
- Supports manual triggering

### 3. **NEW: Iterative Pre-releases (`iterative-prerelease.yml`)**
Creates multiple iterations of pre-release versions with two suffix options:

#### Counter-based Iterations (Default)
- `v1.2.3-pre-1`
- `v1.2.3-pre-2` 
- `v1.2.3-pre-3`
- And so on...

#### Date-based Iterations
- `v1.2.3-pre-20241208`
- `v1.2.3-pre-20241208-1430` (if same day)

#### Triggering Options:

**Manual Trigger:**
1. Go to Actions → "Create Iterative Pre-release"
2. Click "Run workflow"
3. Enter base version (e.g., `v1.2.3` or `1.2.3`)
4. Choose counter-based or date-based suffix
5. Run the workflow

**Automatic Trigger:**
- Triggered on pushes to `main` or `develop` branches
- Only when code in `lib_version/`, `setup.py`, or `pyproject.toml` changes
- Uses latest stable release as base version

#### Examples:

```bash
# Install specific iteration
pip install git+https://github.com/remla25-team8/lib-version.git@v1.2.3-pre-2

# Install latest stable
pip install git+https://github.com/remla25-team8/lib-version.git@v1.2.3
```

## Version Management Strategy

1. **Stable releases**: `v1.2.3` (manual tags)
2. **Standard pre-releases**: `v1.2.4-pre` (auto-created after stable release)
3. **Iterative pre-releases**: `v1.2.3-pre-1`, `v1.2.3-pre-2`, etc. (multiple iterations for testing)

This approach allows for:
- Continuous testing with multiple pre-release iterations
- Clear separation between stable and pre-release versions
- Flexible versioning schemes (counter or date-based)
- Automated and manual release management

## Development

```bash
# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Build package
python -m build
```

## Requirements

- Python >=3.9
- setuptools_scm for version management
- build tools for packaging
