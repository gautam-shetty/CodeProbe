import os

import config as cfg

absoulte_path = os.path.dirname(os.path.abspath(__file__))

def readFile(file_path):
    absolute_file_path = absoulte_path + file_path
    file_content = open(absolute_file_path).read()
    return file_content

def bytesOfFile(file_path):
    file_content = readFile(file_path)
    return bytes(file_content, cfg.FILE_ENCODING)