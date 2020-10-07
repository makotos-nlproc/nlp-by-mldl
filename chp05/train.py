from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

from preprocessing import clean_html, tokenize
from utils import load_dataset, train_and_eval


def main():
    x, y = load_dataset('data/amazon_reviews_multilingual_JP_v1_00.tsv', n=5000)
    