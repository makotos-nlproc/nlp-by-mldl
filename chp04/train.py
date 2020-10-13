from sklearn.model_selection import train_test_split

from preprocecessing import clean_html, normalize_number, tokenize, tokenize_base_form
from utils import load_dataset, train_and_eval


def main():
    x, y = load_dataset('data/amazon_reviews_multilingual_JP_v1_00.tsv', n=100)
    x_train, x_test , y_train, x_test = tarin_test_splite(x, y,
                                                          test_size=0.2,
                                                          random_state=42)
    
    print('Tokenization only.')
    tarin_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize)

    print('Clean html.')
    tarin_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize, preprocessor=clean_html)

    print('Normalize number')
    tarin_and_eval(x_train, y_train, x_test, y_test, tokenize=normalize_number)

    print('Base form.')
    tarin_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize_base_form)

    print('Lower text.')
    tarin_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize, loercase=True)