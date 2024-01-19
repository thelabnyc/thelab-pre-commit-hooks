from __future__ import annotations

import argparse
import pathlib
import re
from datetime import date
from typing import Sequence


def update_year(
    file: pathlib.Path,
    pattern: re.Pattern,
) -> bool:
    def _repl(matchobj):
        match = matchobj.group(0)
        year = matchobj.group("year")
        return match.replace(year, str(date.today().year))

    orig_license = file.read_text()
    new_license = pattern.sub(_repl, orig_license)
    if orig_license == new_license:
        return False

    file.write_text(new_license)
    return True


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        type=pathlib.Path,
        help="path to license file",
        default="LICENSE",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        type=str,
        help=(
            "regex pattern for finding the copyright year. Must contain the "
            "named group `year`"
        ),
        default=r"\[?(?P<year>\d{4})\]?\sthelab",
    )
    args = parser.parse_args(argv)
    did_update = update_year(
        file=args.file,
        pattern=re.compile(args.pattern),
    )
    return int(did_update)


if __name__ == "__main__":
    raise SystemExit(main())
