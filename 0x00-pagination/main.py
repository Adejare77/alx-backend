#!/usr/bin/env/ python3
import csv
import json


def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)

make_json('baby_names.csv', 'baby_names.json')
