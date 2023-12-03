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
        if row[3] == "labels":
            writer.writerow(row)
        else:
            assignees = json.loads(row[2])
            assignees_names = [
                x["login"] for x in assignees
            ]
            row[2] = " ".join(assignees_names)
            labels = json.loads(row[3])
            bounty_names = [
                x["name"] for x in labels if RE_BOUNTY_NAME.search(x["name"])
            ]
            row[3] = " ".join(bounty_names)
            writer.writerow(row)


if __name__ == "__main__":
    main()

