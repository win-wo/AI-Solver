"""This module is use to read file"""
import os

def file_reader(file_path):
    """read the file in the path then return result in string"""
    path = os.path.join(os.path.dirname(__file__), file_path)
    print("reading: " + file_path)
    file = open(path, "r", encoding="utf8")
    result = file.read()
    file.close()
    return result
