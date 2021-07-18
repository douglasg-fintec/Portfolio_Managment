# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(data, csv_path, header=None):
    """Saves the qualifying loans to a CSV file.

    Args:
        csvpath (Path): The csv file path.
        data (list of lists): The data to be written to the CSV file.
        header (list): Optional row to be added as header in the csv

    Returns:
        Nothing.
    """
       # Open a new CSV file.

    #NOTE "closedfd=True to ensure the file is closed properly"
    with open(csv_path, 'w',newline = '', closefd=True) as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
 
        # write the header row if it contains values
        if (header):
            csv_writer.writerow(header)
        # write the values in each row each row 
        for row in data:
        # write the values from each row to the csv file
            csv_writer.writerow (row)  

