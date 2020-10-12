import re


from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
t = Tokenizer()

def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(strip=strip)


def tokenize(text):
    return t.tokenize(text, wakati=True)


def tokenize_base_form(text):
    return [token.base_form for token in t.tokenize(text)]


def normalize_number(text, reduce=False):
    if reduce:
        normalized_text = re.sub(r'\d+', '0', text)
    else:
        normalized_text = re.sub(r'\d', '0', text)
    return normalized_text
