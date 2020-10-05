import string
import pandas as pd


def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text / len(text))
    return rate <= threshold


def load_dataset(filename, n=500, state=6):
    df = pd.read_csv(filename, sep='\t')
    