"""
Util script for changing label of a sample.
Use when collected sample is mislabeled.
Usage: change_sample_label.py [FILENAME] [LABEL]
"""

import sys
import numpy as np
import pandas as pd

from config import *

def change_label(filename, label):
    """
    Take as input a filename (sample to be changed)
    and a proper label. Save the sample and return it.
    """
    if label not in LABELS_NAMES:
        raise NameError
        print("Incorrect label")
        exit()

    try:
        data = pd.read_pickle(DATA_TEMP_DIR + file_name)
        data_changed = change_label(data, label)
        data_changed.to_pickle(DATA_TEMP_DIR + 'sample_changed.pckl')
    except NameError:
        raise NameError

    for i in data.index: # pragma: no cover
        data.at[i, COLUMN_NAMES[0]] = label
    return data

if __name__ == '__main__': # pragma: no cover
    if(len(sys.argv) != 3):
        print("Usage: change_sample_label.py [FILENAME] [LABEL]")
        exit()

    filename = sys.argv[1]
    label = sys.argv[2]

    change_label(filename, label)
