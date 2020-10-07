import string
import pandas as pd
from sklearn.linear_model import logisticRegression
from sklearn.metrics import accuracy_score


def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text / len(text))
    return rate <= threshold


def load_dataset(filename, n=500, state=6):
    df = pd.read_csv(filename, sep='\t')

    # マルチクラスから二値クラスへ変換
    mapping = {1: 0, 2: 0, 4: 1, 5: 1}
    df = df[df.star_rating != 3]
    df.star_rating = df.star_rating.map(mapping)

    # 日本語テキストを抽出
    is_jp = df.review_body.apply(filter_by_ascii_rate)
    df = [is_jp]

    df = df.sample(frac=1, random_state=state)
    grouped = df.groupby('star_rating')
    df = grouped.head(n=n)
    return df.review_body.values, df.star_rating.values


def train_and_eval(x_train, y_train, x_test, y_test, vectorizer):
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)
    clf = logisticRegression(solver='liblinear')
    clf.fit(x_test_vec, y_train)
    y_pred = clf.predict(x_test_vec)
    score = accuracy_score(y_test, y_pred)
    print('{:.4f}'.format(score))
    