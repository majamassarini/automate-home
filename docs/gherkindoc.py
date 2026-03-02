#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini
"""
Convert Gherkin ``.feature`` files to Sphinx RST documentation pages.

Usage::

    python3 gherkindoc.py <input_dir> <output_dir>

For every ``*.feature`` file found directly inside *input_dir* an RST file
named ``{input_dir_name}.{stem}.feature-file.rst`` is written to *output_dir*.
The RST file embeds the feature source in a ``code-block:: gherkin`` directive.
"""

import sys
from pathlib import Path


def feature_to_rst(feature_file: Path, out_dir: Path, prefix: str) -> None:
    """Write an RST page for *feature_file* into *out_dir*.

    :param feature_file: path to the ``.feature`` source file
    :param out_dir: directory where the RST file will be written
    :param prefix: name of the input directory used as the RST filename prefix
    """
    name = feature_file.stem
    rst_name = f"{prefix}.{name}.feature-file.rst"

    content = feature_file.read_text(encoding="utf-8")
    title = name.replace("_", " ")
    indented = "\n".join("   " + line for line in content.splitlines())

    rst = (
        f"{title}\n"
        f"{'=' * len(title)}\n"
        f"\n"
        f".. code-block:: gherkin\n"
        f"\n"
        f"{indented}\n"
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / rst_name).write_text(rst, encoding="utf-8")


def main() -> None:
    if len(sys.argv) < 3:
        print(
            f"Usage: {sys.argv[0]} <input_dir> <output_dir>", file=sys.stderr
        )
        sys.exit(1)

    in_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])

    for feature_file in sorted(in_dir.glob("*.feature")):
        feature_to_rst(feature_file, out_dir, in_dir.name)


if __name__ == "__main__":
    main()
