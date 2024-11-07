from pathlib import Path

__package_version = "unknown"


def get_package_version() -> str:
    """Find the version of this package."""
    global __package_version

    if __package_version != "unknown":
        return __package_version

    import toml

    pyproject_toml_file = Path(__file__).parent.parent / "pyproject.toml"
    if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
        __package_version = toml.load(pyproject_toml_file)["tool"]["poetry"]["version"]
    return __package_version


version = get_package_version()
release_date = "unknown"
commit = "unknown"
builder = "unknown"
