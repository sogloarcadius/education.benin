#! /usr/bin/py
# -*- coding:utf8 -*-

import os
import yaml
import json

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

OPENDATA_DIR = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR)))

DATA_DIR = os.path.join(os.path.dirname(OPENDATA_DIR), "data")

EMERGENCY_DATASET_PATH = os.path.join(DATA_DIR, "emergency.yml")

FACULTIES_DATASET_PATH = os.path.join(DATA_DIR, "faculties.yml")

PROVINCES_DATASET_PATH = os.path.join(DATA_DIR, "provinces.yml")

UNIVERSITIES_DATASET_PATH = os.path.join(DATA_DIR, "universities.yml")

COURSES_DATASET_PATH = [
    os.path.join(DATA_DIR, 'formations', x) for x in os.listdir(os.path.join(DATA_DIR, 'formations'))
]


def get_emergency():
    with open(EMERGENCY_DATASET_PATH) as fp:
        data = yaml.safe_load(fp)
        
    return data


def get_faculties():
    with open(FACULTIES_DATASET_PATH) as fp:
        data = yaml.safe_load(fp)
        
    return data


def get_provinces():
    with open(PROVINCES_DATASET_PATH) as fp:
        data = yaml.safe_load(fp)
        
    return data


def get_universities():
    with open(UNIVERSITIES_DATASET_PATH) as fp:
        data = yaml.safe_load(fp)
        
    return data


def get_courses():
    courses = []
    for file in COURSES_DATASET_PATH:
        with open(file, 'r+') as fp:
            current_file_content = yaml.safe_load(fp)
        current_courses = current_file_content["courses"]
        for course in current_courses:
            course["university"] = current_file_content["id"]
        courses += current_courses 

