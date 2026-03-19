#!/usr/bin/python3
"""
python-serialization.task_02_csv
"""
import csv
import json


def convert_csv_to_json(filename):
    if filename == "":
        return False
    with open(filename, "r") as csvfile:
        data = list(csv.DictReader(csvfile))

    with open(data, "w") as jsonfile:
        return json.dump(data, jsonfile)
