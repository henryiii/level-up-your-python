#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["nbformat"]
# ///

import argparse
from pathlib import Path
import nbformat


def update_notebook(path: Path) -> None:
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)

    nb.metadata["kernelspec"] = {
        "name": "python3",
        "display_name": "Python 3  (ipykernel)",
        "language": "python",
    }

    nbformat.write(nb, path)
    print(f"Updated {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)

    args = parser.parse_args()
    for path in args.paths:
        update_notebook(path)


if __name__ == "__main__":
    main()
