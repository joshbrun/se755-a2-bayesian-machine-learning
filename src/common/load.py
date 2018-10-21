# coding=utf-8

"""
SE755 - A2
Loads in the data from csv files

Authors:
Joshua Brundan
Kevin Hira
"""

import pandas


def load(path, has_header):
    """
    Loads in the data from a csv file.
    :param path: The path to the data
    :param has_header: Has a header or not
    :return:
    """
    if has_header:
        header = 0
    else:
        header = None

    raw_data = pandas.read_csv(path, header=header)

    print("Data:")
    print(raw_data.describe())
    print(path)

    return raw_data