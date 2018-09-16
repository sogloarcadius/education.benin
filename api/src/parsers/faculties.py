#! /usr/bin/py
# -*- coding:utf8 -*-

"""
Prepare faculties list data
"""

import os
import yaml
import json

from parsers import API_DIR


FILE_PATH = os.path.join(os.path.join(API_DIR, "data", "yaml"), "facultes.yml")
DEST_DIR = os.path.join(os.path.dirname(API_DIR), "app", "src", "store")


def read_yaml_file():
    with open(FILE_PATH) as fp:
        data = yaml.safe_load(fp)
    return data


def main():
    faculties = read_yaml_file()
    with open(os.path.join(DEST_DIR, "faculties.json"), "w") as fp:
        json.dump(faculties, fp)

if __name__ == "__main__":
    main()