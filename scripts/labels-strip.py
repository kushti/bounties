#!/usr/bin/env python3
import csv
import fileinput
import json
import re
import sys

RE_BOUNTY_NAME = re.compile(r"^(B-|Bounty)")


def main() -> None:
    reader = csv.reader(fileinput.input(encoding="utf-8"))
    writer = csv.writer(sys.stdout)
    for row in reader:
        if row[2] == "labels":
            writer.writerow(row)
        else:
            labels = json.loads(row[2])
            bounty_names = [
                x["name"] for x in labels if RE_BOUNTY_NAME.search(x["name"])
            ]
            row[2] = " ".join(bounty_names)
            writer.writerow(row)


if __name__ == "__main__":
    main()

